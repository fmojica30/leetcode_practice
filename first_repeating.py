#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            repeats = False
            for j in range(i + 1, len(s)):
                if (s[i] == s[j]):
                    repeats = True
                    continue
            if repeats:
                continue
            elif (not repeats and i != len(s) - 1):
                return i
            
        return -1


def main():
    x = Solution()

    print(x.firstUniqChar("cc"))


main()
