n = int(input("Print your number: "))
class gen:
    def __init__(self, n):
        self.start = 0
        self.end = n + 1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.end > self.start):
            self.end-=1
            return self.end
        else:
            raise StopIteration
generator = iter(gen(n))
for x in generator:
    print(x)