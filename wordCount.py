def count_words(sentence):
    words = sentence.split()
    num_words = len(words)
    return num_words


user_input = input("Enter a sentence: ")
print("Number of words:", count_words(user_input))
