class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        from collections import Counter
        
        counts = Counter(ages)
        ans = 0
        
        for age_a, count_a in counts.items():
            for age_b, count_b in counts.items():
                if age_b <= 0.5 * age_a + 7:
                    continue
                if age_b > age_a:
                    continue
                if age_b > 100 and age_a < 100:
                    continue
                
                ans += count_a * count_b
                if age_a == age_b:
                    ans -= count_a
                    
        return ans