class EvaluationOfPostfix():

    def __init__(self, postfix):
        self.postfix = list(postfix)
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def operators(self, c):
        return c in "+-*/^%"

    def evaluate(self):
        if len(self.postfix) == 0:
            return "Empty expression"

        for i in self.postfix:
            if not self.operators(i):
                self.stack.append(i)
            else:
                if self.isEmpty():
                    return "Stack is Empty"
                else:
                    a = self.stack.pop()
                    b = self.stack.pop()
                    temp = str(eval(b + i + a))
                    self.stack.append(temp)

        if len(self.stack) == 1:
            return self.stack[0]
        else:
            return "Invalid expression"

# Driver's code
if __name__ == "__main__":
    obj = EvaluationOfPostfix("22*3+")
    print(obj.evaluate())
