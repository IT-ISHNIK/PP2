N = int(input("Write your number: "))
class GENERATOR:
    def __init__(self, N):
        self.N = N
        self.value = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.value+=3
        if(self.value <= self.N):
            return self.value
        else:
            raise StopIteration
class GENERATOR1:
    def __init__(self, N):
        self.N = N
        self.value = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.value+=4
        if(self.value <= self.N):
            return self.value
        else:
            raise StopIteration
gen = iter(GENERATOR(N))
gen1 = iter(GENERATOR1(N))
for x in gen:
    print(x)
for x in gen1:
    print(x)

