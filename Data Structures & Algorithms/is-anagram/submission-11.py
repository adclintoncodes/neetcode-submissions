class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #Change the data structure to dictionary!
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
       
    #     dict1 = {}
    #     dict2 = {}

    #     for i in range(len(s)):
    #         if s[i] not in dict1.keys():
    #             dict1[s[i]] = 1
    #         else:
    #             dict1[s[i]] += 1

    #     for i in range(len(t)):
    #         if t[i] not in dict2.keys():
    #             dict2[t[i]] = 1
    #         else:
    #             dict2[t[i]] += 1
    #     print(f"Dict1: {dict1}, Dict2 {dict2}")

    #     for key in dict1:
    #         if key not in dict2.keys():
    #             return False

    #         if dict1[key] != dict2[key]:
    #             print(f"{dict2[key]}")
    #             return False
    #         else:
    #             is_anagram = True
    # return is_anagram
            
