import java.util.*;

class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);   // prefixSum -> frequency

        int prefixSum = 0;
        int count = 0;

        for (int num : nums) {
            prefixSum += num;

            if (freq.containsKey(prefixSum - k)) {
                count += freq.get(prefixSum - k);
            }

            freq.put(prefixSum, freq.getOrDefault(prefixSum, 0) + 1);
        }

        return count;
    }
}
