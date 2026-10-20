class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #data structure is dictionary
        # initiate a dictionary and keep the count of all the numbers in the list.
        #loop through the value of the key-value pairs in the dictionary if any > 1, return true
        #else: return false.

        new_dict = {}
        #Converting a list into a dictionary
        for i in nums:
            if i not in new_dict.keys():
                new_dict[i] = 1
            else:
                new_dict[i] += 1

        for key in new_dict:
            if new_dict[key] > 1:
                return True
        return False




        