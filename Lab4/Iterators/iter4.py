"""Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print 
each of the yielded values."""
a = int(input("Beginning value: "))
b = int(input("End value: "))
class gen:
    def __init__(self, a, b):
        self.start = a-1
        self.end = b
    def __iter__ (self):
        return self
    def __next__(self):
        if(self.start < self.end):
            self.start+=1
            return self.start **2
        else:
            raise StopIteration
generator = iter(gen(a,b))
for x in generator:
    print(x)
for i in range(a,b+1):
    print(i**2)
    i+=1
