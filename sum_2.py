#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution():
    def two_sum(self, arr, total):
        dic = {}
        for i in range(len(arr)):
            diff = total - arr[i]
            if diff in dic.keys():
                return [i, dic[diff]] 
            else:
                dic[arr[i]] = i

        return -1


def main():
    arr = [1,2,3,4,5,6,7,8,9]
    x = Solution()
    print(x.two_sum(arr, 8))

main()
            
