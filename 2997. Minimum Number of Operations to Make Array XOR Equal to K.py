class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        flip_count = 0
        xor_sum = 0
        for data in nums:
            xor_sum ^= data
        
        for i in range(32):
            bit_mask = 1 << i
            one_bit_count = 0
            
            if (xor_sum & bit_mask) != (k & bit_mask):
                flip_count += 1
        
        return flip_count
