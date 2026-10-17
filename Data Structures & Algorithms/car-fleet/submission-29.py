class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [] # (position,time pairs)
        # for i in poition:
        # calculate time
        # append position,time to data

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            pairs.append([position[i],time])
        
        pairs.sort(key = lambda pair : pair[0])

        idx = len(pairs) - 1
        # print(pairs)
        while idx > 0:
            if pairs[idx-1][1] <= pairs[idx][1]:
                pairs.pop(idx-1)
            idx -= 1
        return len(pairs)



        