class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create a list output which keeps the number of days. 
        # loop through the length of the list. 
        # set a variable high that will keep track the index  of the highest temperature after the i-th iteration
        #check if the (i+1)th candidate is greater than i, if true, 
        # set high = i+1 
        # update the list of return by output[i] = high - i
        # else update the list of return by ouput[i] =0
        # return output

        output = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
               StackTemp, StackInd = stack.pop()
               output[StackInd] = i-StackInd

            stack.append([t, i])
        
        return output










        # for i in range(n):
        #     for j in range(i+1, n):                    
        #         if temperatures[j] > temperatures[i]:
        #             high_temp_index = j
        #             output[i] = high_temp_index-i
        #             break 
        #         else:
        #             output[i] = 0
        # return output  
#in the second nested for loop, if the highest temperature was found, 
#you don't need to keep going. you need to break. hence the break on the line22.

#And also range(n) returns value from 0 to (n-1)!

#implement using stack

        # stack = [] 
        # stack.append(temperatures[0])
        # n = len(temperatures)

        # for i in range(n):
        #     if tempertures[i]  > 








    
        