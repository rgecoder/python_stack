class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *num):
        for i in range(0, len(num)):
            # Check if list or tuple
            if type(num[i]) is list or type(num[i]) is tuple:
                # unpack if list or tuple and increment
                for j in num[i]:
                    self.total += j
            else:
                self.total += num[i]
        # print self.total
        return self

    def subtract(self, *num):
        for i in range(0, len(num)):
            # check if list or tuple
            if type(num[i]) is list or type(num[i]) is tuple:
                # unpack if list or tuple and increment
                for j in num[i]:
                    self.total -= j
            else:
                self.total -= num[i]
        return self

    def result(self):
        print (self.total)

        return self




x = MathDojo.add(2).result()