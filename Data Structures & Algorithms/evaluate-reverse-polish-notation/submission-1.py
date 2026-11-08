class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 3:
            return int(tokens[0])
        stack=[]
        operators = {"+","-","*","/"}
        stack.append(int(tokens[0]))
        for i in range(1,len(tokens)):
            num=tokens[i]
            if num in operators:
                b=int(stack.pop())
                a=int(stack.pop())
                match num:
                    case "+":
                        b=a+b
                    case "-":
                        b=a-b
                    case "*":
                        b=a*b
                    case "/":
                        b=a/b
                    case _:
                        return None
                stack.append(b)
            else:
                stack.append(int(num))
        return int(stack.pop())