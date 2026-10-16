class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #initiate a stack. using the deque. 
        #get the length of the input list
        #set a variable eval which tracks the answer of the operations.
        #iterate through the array using range
        #cast every string into an integer. 
        #check if the current item in the array is a number using isdigit. 
        #append to stack if yes. 
        #else check if it is +,
        #if yes, store the last value of stack in a variable a = stack.pop()
        #store the next in b = stack.pop()
        #apply the + operand to a & b. 
        #repeat the conditionals for the rest. 

        stack = deque()
        length = len(tokens)
        eval = 0
        for i in range(length):
            if tokens[i][1:].isdigit() or tokens[i].isdigit():
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "+":
                    eval = a + b 
                elif tokens[i] == "-":
                    eval = b-a
                elif tokens[i] == '*':
                    eval = a*b
                elif tokens[i] == '/':
                    eval = int(b/a)
                stack.append(eval)
        return stack.pop()
        









        