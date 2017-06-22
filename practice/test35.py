# encoding:utf-8
# author:wwg

def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                # nums[j] = nums[j+1]
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                print nums
    return nums

nums = [55,3,45,6,8,2,11]

print bubbleSort(nums)