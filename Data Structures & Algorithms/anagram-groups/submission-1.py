class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #use a dictionary. 
        #use the sorted strings as keys, and their values will be a list of its valid anagrams
        sorted_strs = defaultdict(list)
        print(sorted_strs)
        for i in strs:
            sorted_string = "".join(sorted(i))

            sorted_strs[sorted_string].append(i)
    
        #print(sorted_strs)

        return list(sorted_strs.values())
 



        

 




