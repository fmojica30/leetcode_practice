#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def subsets(self, nums):
        if not nums:
            return []
        self.res = []
        self.dfs(nums, [], 0)
        return self.res

    def dfs(self, nums, temp, index):
        if (index == len(nums)):
            self.res.append(temp[:])
            return

        temp.append(nums[index])
        self.dfs(nums, temp, index + 1)
        temp.pop()
        self.dfs(nums, temp, index + 1)


class Parentheses:
    def valid(self, n):
        left_remain = right_remain = n
        result = []
        self.dfs(left_remain, right_remain, 2 * n, result, [])
        return result

    def dfs(self, left_remain, right_remain, size, result, temp):
        if len(temp) == size:
            result.append("".join(temp))

        if left_remain > 0:
            temp.append('(')
            self.dfs(left_remain - 1, right_remain, size, result, temp)
            temp.pop()

        if right_remain > 0 and right_remain > left_remain:
            temp.append(')')
            self.dfs(left_remain, right_remain - 1, size, result, temp)
            temp.pop()

def isPalindrome(s):
    check = [] 
    position = -1

    for i in range(len(s)):
        check.append(s[position])
        position -= 1

    if (s == "".join(check)):
        return True

    return False


def main():
    x = Solution()
    y = [1, 2, 3]
    print(sum(y))
    print("subsets: " + str(x.subsets(y)))

    a = Parentheses()
    b = 4
    print("parentheses: " + str(a.valid(3)))

    print("Palindrome: " + str(isPalindrome("racecar")))

main()
