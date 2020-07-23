'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


# def sliding_window_max(nums, k):
#     # Your code here
#     i = 0
#     arr = []
#     while i + k - 1 < len(nums):
#         arr.append(max(nums[i:(i+k)]))
#         i += 1

#     return arr


class Node():
    def __init__(self, value: int):
        self.left = None
        self.right = None

    def set_left(self, node: "Node") -> None:
        self.left = node.

    def set_right(self, node: "Node") -> None:
        self.right = node


class MaxTree():
    def __init__(self, )


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
