#Expression infix to postfix
class Conversion:
    def __init__(self):
        self.stack = []
        self.result=[]
        self.precedence ={
            '(':0,
            '+':1,
            '-':1,
            '*':2,
            '/':2,
            '^':3,
        }
    def push(self,ele):
        self.stack.append(ele)
    def isEmpty(self):
        return self.stack ==  []        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return '$'
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return "$"        
    def notGreater(self,ele):
        try:
            a= self.precedence[self.peek()]
            b= self.precedence[ele]

            return True if a >= b else False
        except KeyError:
            return False 
    def infixToPostfix(self,exp):
        for ele in exp:
            if ele.isalnum():
                self.result.append(ele)
            elif ele == '(':
                self.push(ele)
            elif ele == ')':
                x = self.pop()
                while x!= '(':
                    self.result.append(x)
                    x = self.pop()
            else:
                while (not self.isEmpty() and self.notGreater(ele)):
                    self.result.append(self.pop())
                self.push(ele)
        while not self.isEmpty():
            self.result.append(self.pop())
        return "".join(self.result)

c = Conversion()
result = c.infixToPostfix("(2*3+4*(5-8+12))")
print(result)
