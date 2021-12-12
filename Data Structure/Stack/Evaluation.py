#postfix evaluation
class Evaluation:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack ==  []
    def push(self,op):
        self.stack.append(op)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return "$"
    def evaluatePostFix(self,exp):
        for c in exp:
            if c.isdigit():
                self.push(c)
            else:
                a = self.pop()
                b = self.pop()
                self.push(str(eval(b+c+a)))
        return int(self.pop())

e = Evaluation()
print(e.evaluatePostFix('231*+9-'))




            