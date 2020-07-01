#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        temp = []
        self.result = []
        position = 1
        self.helper(n, k, position, temp)
        return self.result
    
    def helper(self, n, k, position, temp):
        if (len(temp) == k):
            print(temp)
            self.result.append(temp)
            return 
        
        if (position > n):
            return 
        
        temp.append(position)
        self.helper(n, k, position + 1, temp)
        
        temp.pop()
        self.helper(n, k, position + 1, temp)


x = Solution()

print(x.combine(4,2))
