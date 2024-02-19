#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console
N = int(input("Print your number: "))
class GENERATOR:
    def __init__(self,N):
        self.N = N
        self.value = -2
    def __iter__(self):
        return self
    def __next__(self):
        self.value+=2
        if(self.value <= N):
            return self.value
        else:
            raise StopIteration
gen = iter(GENERATOR(N))
ll = []
for x in gen:
    ll.append(x)
print(ll)
    
        