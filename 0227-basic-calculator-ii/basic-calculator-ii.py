class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operation = '+'
        curr = 0
        for i in range(len(s)):
            if s[i].isdigit():
                curr = curr * 10 + int(s[i])
            if i == len(s) - 1 or (s[i].isdigit() == False and s[i] != ' '):

                if operation == '+':
                    stack.append(curr)
                elif operation == '-' :
                    stack.append(-curr)
                elif operation == '*':
                    stack.append(stack.pop() * curr)
                elif operation == '/':
                    if stack[-1] < 0:
                        stack.append(-(-stack.pop() // curr))
                    else:
                        stack.append(stack.pop() // curr)
                curr = 0
                operation = s[i]
        return sum(stack)
        