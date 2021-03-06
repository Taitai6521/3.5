# import random
#
#
# def in_order(numbers):
#     return (numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
#     for i in range(len(numbers)-1):
#         if numbers[i] > numbers[i+1]:
#             return False
#     return True
#
#
# def bogo_sort(numbers):
#     while not in_order(numbers):
#         random.shuffle(numbers)
#     return numbers
#
# if __name__ == '__main__':
#     print(bogo_sort([1,3,4,9,3]))
# from typing import List
#
#
# def bubble_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         for j in range(len_numbers -1 -i):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#     return numbers
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     import random
#
#     nums = [random.randint(0, 1000) for i in range(10)]
#     print(bubble_sort(nums))

from typing import List

# def bubble_sort(numbers):
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         for j in range(len_numbers - 1 -i):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#     return numbers
# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0,1000) for i in range(10)]
#     print(bubble_sort(nums))

from typing import List

# def bubble_sort(numbers):
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         for j in range(len_numbers -1 -i):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#
#     return numbers
# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0,1000) for i in range(10)]
#     print(bubble_sort(nums))
#
#
# def cocktail_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     swapped = True
#     start = 0
#     end = len_numbers -1
#     while swapped:
#         swapped = False
#         for i in range(start, end):
#             if numbers[i] > numbers[i+1]:
#                 numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#                 swapped = True
#         if not swapped:
#             break
#
#         swapped = False
#
#         end = end - 1
#         for i in range(end-1, start-1, -1):
#             if numbers[i] > numbers[i + 1]:
#                 numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#                 swapped = True
#         start = start + 1
#     return numbers
#
#
# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0, 1000) for i in range(10)]
#     print(cocktail_sort(nums))
#
#
#









from typing import List

# def cocktail_sort(numbers):
#
#     len_numbers = len(numbers)
#     start = 0
#     end = len_numbers -1
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len_numbers):
#             if numbers[i] > numbers[i+1]:
#
#                 numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#             swapped = True
#         if not swapped:
#             break
#         swapped = False
#
#
#
#         end = end - 1
#         for i in range(start-1, end-1,-1):
#         if numbers[i] > numbers[i + 1]:
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#         swapped = True
#         start = start + 1
#     return numbers
#
#
#
# if __name__ == '__main__':
# nums = [11, 4,5, 5,6,3]
# print(cocktail_sort(nums))

from typing import List
# def comb_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     gap = len_numbers
#     swapped = True
#
#     while gap != 1 or swapped:
#         gap = int(gap / 1.3)
#         if gap < 1:
#             gap = 1
#         swapped = False
#         for i in range(0, len_numbers-gap):
#             if numbers[i] > numbers[i+gap]:
#
#                 numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]
#                 swapped = True
#     return numbers
#
# if __name__ == '__main__':
#     nums =[1, 3, 5, 5,4,2,2]
#     print(comb_sort(nums))

#
# from typing import List
#
# def selection_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         min_idx = i
#         for j in range(i+1, len_numbers):
#             if numbers[min_idx] > numbers[j]:
#                 min_idx = j
#         numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
#
#     return numbers
#
#
# if __name__ == '__main__':
#     nums = [1, 5, 34, 4 ]
#     print(selection_sort(nums))

from typing import List
#
# def selection_sort(numbers: List[int]) ->List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         min_idx = i
#         for j in range(i+1, len_numbers):
#             if numbers[min_idx] > numbers[j]:
#                 min_idx = j
#
#         numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
#
#     return numbers
#
# if __name__ == '__main__':
#     nums = [1,3,43,4]
#     print(selection_sort(nums))
from typing import List
# def gnome_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     index = 0
#     while index < len_numbers:
#         if index == 0:
#             index += 1
#         if numbers[index] >= numbers[index-1]:
#             index += 1
#         else:
#             numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
#             index -= 1
#     return numbers
# if __name__ == '__main__':
#     nums = [2,1, 3, 4,2,19]
#     print(gnome_sort(nums))


# def insertion_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(1, len_numbers):
#         temp = numbers[i]
#         j = i - 1
#         while j >= 0 and numbers[j] > temp:
#             print(j, end=' ')
#             j -= 1
#
#
#     return numbers
#
#
# if __name__ == '__main__':
#     nums = [13,34,455,5,566,6


from typing import List
#
# def bucket_dort(numbers: List[int], max_num = ) -> List[int]:
#     max_num = max(numbers)
#     len_numbers = len(numbers)
#     size = max_num // len_numbers
#     buckets = [[] for _ in range(size)]
#     for num in numbers:
#         i = num // size
#         if i != size:
#             buckets[i].append(num)
#         else:
#             buckets[size-1].append(num)
#     for i in range(size):
#         insertion_sort(buckets[i])
#     result = []
#     for i in range(size):
#         result += buckets[i]
#     return result


# def shell_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     gap = len_numbers // 2
#
#     while gap > 0:
#         for i in range(gap, len_numbers):
#             temp = numbers[i]
#             j = i
#             while j >= gap and numbers[j-gap] > temp:
#                 numbers[j] = numbers[j-gap]
#                 j -= gap
#             numbers[i] = temp
#         gap //=2
#
#     return numbers
#
#
# if __name__ == '__main__':
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     import random
#     nums = [random]
#
# from typing import List
# def counting_sort(numbers:List[int])-> List[int]
#     max_num = max(numbers)
#     counts = [0] * (max_num + 1)
#     result = [0] * len(numbers)
#
#
# for num in numbers:
#     counts[num] +=  1
#
# if __name__ =='__main__':
#     counting_sort(nums)

#
# def radix_sort(numbers: List[int], place: int) -> List[int]:
#     max_num = max(numbers)
#     place = 1
#     while max_num > place:
#         numbers = counting_sort(numbers, place)
#         place *= 10
#         return numbers

# def partition(numbers: List[int]), low: int, high: int) -> int:
#     pass
#
# def quick_sort(numbers: List[int]) -> List[int]:
#     def _quick_sort(numbers: List[int], low: int, high: int) -> None:
#         if low < high:
#
#         partition_index = partition(numbers, low, high)
#         _quick_sort(numbers, low, partition_index-1)
#         _quick_sort(numbers, partition_index+1, high)
#
#
#
# if  __name__ == '__main__':
#     nums = [1, 9, 9, 0]


def partition(numbers: List[int], low: int, high:: int) -> int:

    i = low -1
    pivot = numbers[high]
    for j in range(low, high):
        if in range[j] <= pivot:
            if numbers[j] <= pivot:
                i +=1



def quick_sort(numbers: List[int] -> List[int]):
    def _quick_sort(numbers: List[int], high: int ) -> None:
        if low < high:


            partition_index = partition(numbers, low, high)

            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(umbers, partition_index+1, high)


    _quick_sort(numbers, 0, len(numbers)-1)

    return numbers