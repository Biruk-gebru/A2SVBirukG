# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:  
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:  
        dic_s = defaultdict(int)  
        
        for elem in cpdomains:  
            count, domain = elem.split() 
            count = int(count) 
            domains = domain.split(".") 
            
            
            for i in range(len(domains)):  
                subdomain = ".".join(domains[i:]) 
                dic_s[subdomain] += count  

        result = [f"{count} {subdomain}" for subdomain, count in dic_s.items()]  
        return result  