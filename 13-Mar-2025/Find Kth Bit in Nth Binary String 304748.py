# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def build(n):
            l=2*n+1
            built_ar=["0"]
            for _ in range(n):
                temp=built_ar[::-1]
                built_ar+=("1")
                for j in range(len(temp)):
                    if temp[j]=="1":
                        built_ar.append("0")
                    else:
                        built_ar.append("1")
            return built_ar
        sol=build(n)
        return sol[k-1]
        

                
        