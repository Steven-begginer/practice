# this small project is very useful for me!
# split the sentence into every single words.
def get_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text.split()

# save as a new text file.
def save_counts(counts):
    with open("wordcounts.txt", "w", encoding="utf-8") as f:
        for word, count in counts.items():
            f.write(f"{word}: {count}\n")

# calculate how many repeats are this words within the sentence
def main():
    counts = {}
    words = get_words("simple.txt")
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    save_counts(counts)

if __name__ == "__main__":
    main()

