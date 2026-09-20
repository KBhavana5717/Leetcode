class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_list = list(s)
        left, right = 0, len(s_list) - 1
        
        while left < right:
            # Move left pointer until it hits a vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move right pointer until it hits a vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # Swap the vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            # Move pointers inward
            left += 1
            right -= 1
            
        return "".join(s_list)