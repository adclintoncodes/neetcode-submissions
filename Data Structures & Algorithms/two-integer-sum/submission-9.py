class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        return_list =[]
        n = len(nums)
        for i in range(n):
            current_val = nums[i]
            for j in range(1,n):
                if i != j:
                    if current_val + nums[j] == target:
                        return_list.append(nums.index(current_val))
                        return_list.append(j)
                        return return_list                
            continue