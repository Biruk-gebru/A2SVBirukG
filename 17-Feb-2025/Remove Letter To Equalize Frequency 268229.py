# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:  
    def equalFrequency(self, word: str) -> bool:  
        freq_counter = Counter(word)  
        freq_counts = list(freq_counter.values()) 
        
        freq_set = Counter(freq_counts)  

        if len(freq_set) == 1:  
            return list(freq_set.keys())[0] == 1 or len(freq_counts) == 1  
        
        if len(freq_set) == 2:  
            freq_list = list(freq_set.items())  
            f1, c1 = freq_list[0]  
            f2, c2 = freq_list[1]  
            if (c1 == 1 and (f1 - 1 == f2 or f1 - 1 == 0)) or (c2 == 1 and (f2 - 1 == f1 or f2 - 1 == 0)):  
                return True  

        return False  