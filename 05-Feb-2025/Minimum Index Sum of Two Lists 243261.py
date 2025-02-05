# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:  
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:  
        index_sum_map = defaultdict(list)  
        for i, restaurant in enumerate(list1):  
            if restaurant in list2:  
                index_sum_map[restaurant].append(i + list2.index(restaurant)) 

        min_sum = float('inf')  
        result = []  

        for restaurant, sum_indexes in index_sum_map.items():  
            index_sum = sum_indexes[0]    
            if index_sum < min_sum:  
                min_sum = index_sum  
                result = [restaurant]  
            elif index_sum == min_sum:  
                result.append(restaurant) 

        return result  