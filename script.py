import string
from collections import Counter

def get_user_input():
    choice = input("Select an option:\n1. Enter text manually\n2. Read text from file\nOption: ")
    if choice == "1":
        text = input("Enter text below:\n")
    elif choice == "2":
        filename = input("Enter filename (including file extension):\n")
        try:
            with open(filename, "r") as file:
                text = file.read()
        except FileNotFoundError:
            print("File not found. Please try again.")
            return None
    else:
        print("Invalid input. Please try again.")
        return None
    return text

def process_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def tokenize_text(text):
    sentences = text.split(".")
    words = [sentence.split() for sentence in sentences]
    return words

def text_summarizer(tokenized_text, num_sentences = 2):
    word_count = {}
    for sentence in tokenized_text:
        for word in sentence:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    sentence_scores = {}
    for i, sentence in enumerate(tokenized_text):
        for word in sentence:
            if word in word_count:
                if i in sentence_scores:
                    sentence_scores[i] += word_count[word]
                else:
                    sentence_scores[i] = word_count[word]
    top_sentences = sorted(sentence_scores, key = sentence_scores.get, reverse = True)[:num_sentences]
    summary = " ".join([" ".join(tokenized_text[i]) for i in top_sentences])
    return summary

def main():
    print("Text Summary Generator\nSummary:\n")
    text = get_user_input()
    if text:
        text = process_text(text)
        tokenized_text = tokenize_text(text)
        summary = text_summarizer(tokenized_text)
        print(summary)

if __name__ == "__main__":
    main()
