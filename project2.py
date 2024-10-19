#write a function to find the longest common prefix string amongst an array of strings

def prefix(strs):
    prefix=strs[0]
    for  string in strs[1:]:
        for i in range(len(prefix)):
            if i >= len(string) or string[i] != prefix[i]:
                prefix = prefix[:i]
    return prefix

# Given an aarray of integers nums and an integer target,return indices of the two numbers such that they add up to target


def sum(num,target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return [i,j]
            
#given a collection of numbers,nums that might contain duplicates,return all possible unique permutations in any order


def unique(nums):
    if len(nums) == 1:
        return [nums]
    result= []
    for i in range(len(nums)):
        if nums[i] in nums[:i]:
            continue
    for j in unique(nums[:i]+nums[i+1]):
        result.append([nums[i]]+j)
        return result


