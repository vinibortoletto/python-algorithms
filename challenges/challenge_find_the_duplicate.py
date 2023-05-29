def validate_nums(nums):
    if nums is None or len(nums) <= 1:
        return False

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False


def create_nums_dict(nums):
    nums_dict = dict()

    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    return nums_dict


def find_duplicate(nums):
    if validate_nums(nums) is False:
        return False

    nums_dict = create_nums_dict(nums)
    duplicate_num = False

    for key, value in nums_dict.items():
        if value > 1:
            duplicate_num = key

    return duplicate_num
