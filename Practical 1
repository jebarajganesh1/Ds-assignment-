
    class pract1D:
    def __init__(self, a):
        self.array = a

    def search(self, e):
        if e in self.array:
            return True
        return False

    def sort(self):
        for i in range(len(self.array)):
            lowest_index = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[lowest_index]:
                    lowest_index = j
            self.array[i], self.array[lowest_index] = self.array[lowest_index], self.array[i]
        return self.array

    def merge_el(self,l):
        self.array = self.array + l
        return self.array

    def reverse(self):
        return self.array[::-1]

a = [5,6,7,89,2,5,6,1]
x= pract1D(a)
print(x.sort())
print(x.search(89))
print(x. merge_el([8,5,7,9,3]))
print(x.reverse())
            
