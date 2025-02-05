# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        mp = {
            1:"I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        ans = []
        arr = list(str(num))
        k = 1
        for i in range(len(arr) - 1, -1, -1):
            last = int(arr[i]) * k

            if last == 0:
                k *= 10
                continue
            elif last in mp:
                ans.append(mp[last])
            elif last + k in mp:
                ans.append(mp[last + k])
                ans.append(mp[k])

            elif last % k == 0 and last < k * 5:
                ans.extend([mp[k]] * (last // k))

            elif last % k == 0 and last > k * 5:
                tmp = last - (k * 5)
                ans.extend([mp[k]] * (tmp//k))
                ans.append(mp[k * 5])

            
            k *= 10
        
        return ''.join(reversed(list(map(str, ans))))
