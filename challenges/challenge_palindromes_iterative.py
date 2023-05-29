def is_palindrome_iterative(word):
    if word == "":
        return False

    length = len(word)

    for index in range(1, length + 1):
        first_index = index - 1
        last_index = length - index

        if word[first_index] != word[last_index]:
            return False

        if first_index >= last_index:
            return True
