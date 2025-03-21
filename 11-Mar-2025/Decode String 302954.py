# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_num = 0
        current_str = ''
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                current_num = 0
                while s[i].isdigit():
                    current_num = current_num * 10 + int(s[i])
                    i += 1
            elif s[i] == '[':
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num = 0
                current_str = ''
                i += 1
            elif s[i] == ']':
                num = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + current_str * num
                i += 1
            else:
                current_str += s[i]
                i += 1
        
        return current_str
