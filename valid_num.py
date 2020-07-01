#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution():
    def isNumber(self, s):
        s = s.strip()
        e = None
        for i in range(len(s)):
            if (s[i].isdigit() or s[i] == "." or s[i] in ["+", "-"]):
                continue
            elif (s[i] == "e"):
                e = i
                break
            else:
                return False
        
        if e:
            num1 = s[0:e]
            num2 = s[e + 1:]
            
            valid1 = self.validNumber(num1)
            valid2 = self.validNumber(num2)
            
            if not valid1 and valid2:
                return False

            if (valid1 and valid2):
                if (valid2["decimal"]):
                    return False
                return True

        return self.validNumber(s)
        
                

    def validNumber(self, s):
        sign = 0
        valid_chars = ["-", "+"]
        for i in range(len(s)):
            if (s[i] in valid_chars):
                sign += 1

            if sign > 1:
                return False

        seen_digit = False
        seen_dot = False


        for i in range(sign, len(s)):
            if s[i].isdigit() and not seen_digit:
                seen_digit = True
            elif s[i] == "." and not seen_dot:
                seen_dot = True
            elif s[i] == "." and seen_dot:
                return False
            elif s[i].isdigit():
                continue
            else: 
                return False
            
        if not seen_digit:
            return False
        
        return {"integer": not seen_dot, "decimal": seen_dot} 
        


def main():

    a = Solution()
    print(a.isNumber("123e12"))
    print("abc: " + str(a.isNumber("abc")))
    print("-90e3: " + str(a.isNumber("-90e3")))
    print(" 99e2.5 : " + str(a.isNumber(" 99e2.5 ")))
    print(" --6: " + str(a.isNumber(" --6")))
    print(" 1 a: " + str(a.isNumber(" 1 a")))
    print("95a54e53: " + str(a.isNumber("95a54e53")))
            

main()
        
