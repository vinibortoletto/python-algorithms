def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_string_char_list = list(first_string.lower())
    first_string = merge_sort(first_string_char_list)

    second_string_char_list = list(second_string.lower())
    second_string = merge_sort(second_string_char_list)

    conditional = first_string == second_string
    return (first_string, second_string, conditional)


def merge_sort(char_list):
    if len(char_list) <= 1:
        return "".join(char_list)

    middle = len(char_list) // 2
    left_side_list = merge_sort(char_list[:middle])
    right_side_list = merge_sort(char_list[middle:])

    return merge(char_list, left_side_list, right_side_list)


def merge(char_list, left_side_list, right_side_list):
    left_index = 0
    right_index = 0

    for index in range(0, len(char_list)):
        if left_index >= len(left_side_list):
            char_list[index] = right_side_list[right_index]
            right_index = right_index + 1

        elif right_index >= len(right_side_list):
            char_list[index] = left_side_list[left_index]
            left_index = left_index + 1

        elif left_side_list[left_index] < right_side_list[right_index]:
            char_list[index] = left_side_list[left_index]
            left_index = left_index + 1

        else:
            char_list[index] = right_side_list[right_index]
            right_index = right_index + 1

    return "".join(char_list)
