# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join(["[.]" if e == "." else e for e in address])
        
        