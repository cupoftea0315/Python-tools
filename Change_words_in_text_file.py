def modify_word_file(filename, words_to_change, new_word):
    """
    Modifies a text file by changing specific words to a new word.
    author: GhatGPT
    :param filename: Name of the word file
    :param words_to_change: List of words to change
    :param new_word: New word to replace the specific words
    """
    with open(filename, "r") as file:
        text = file.read()
        for word in words_to_change:
            text = text.replace(word, new_word)
    with open(filename, "w") as file:
        file.write(text)


if __name__ == "__main__":
    filename = "GhatGPT_sample.txt"
    words_to_change = ["apple", "banana"]
    new_word = "fruit"
    modify_word_file(filename, words_to_change, new_word)
