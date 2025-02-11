def merge(left_list:list[int], right_list:list[int]) -> list[int]:  
    sorted_list = []
    left_list_index = right_list_index = 0

    while left_list_index<len(left_list) and right_list_index<len(right_list):
        if left_list[left_list_index] <= right_list[right_list_index]:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

        else:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

    if left_list_index==len(left_list):
        sorted_list+=right_list[right_list_index:]
    
    else:
        sorted_list+=left_list[left_list_index:]

    return sorted_list


def merge_sort(nums:list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2

    left_list = merge_sort(nums[:middle])
    right_list = merge_sort(nums[middle:])

    return merge(left_list, right_list)
