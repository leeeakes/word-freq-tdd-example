from collections import Counter

def clean_text(text):
    text = text.lower()

    disallowed_chars = ",."
    for char in disallowed_chars:
        text = text.replace(char, "")

    return text

def word_frequency(text):
    text = clean_text(text)
    words = text.split()
    freq = Counter(words)
    return freq
