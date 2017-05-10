#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 冒泡排序
def sort_maopao(nums):
    if (isinstance(nums, list)):
        length = len(nums)
        for i in range(length - 1):
            for j in range(length - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                pass
    else:
        raise Exception("parse is not the right type")


# 插入排序
def sort_insert(nums):
    length = len(nums)
    for i in range(1, length):
        temp = nums[i]
        for j in range(i):
            print(nums[i - j - 1], nums[i])
            if nums[i - j - 1] > temp:
                nums[i - j] = nums[i - j - 1]
                nums[i - j - 1] = temp;
                print(nums)
            else:
                break
            pass


nums = [5, 2, 45, 6, 8, 2, 1]
sort_insert(nums)
print(nums)
