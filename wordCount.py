def count_words(sentence):
    words = sentence.split()
  # print words
    num_words = len(words)
    return num_words


# function to count words
user_input = input("Enter a sentence: ")
print("Number of words:", count_words(user_input))..
