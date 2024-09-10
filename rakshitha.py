import time
start=time.time()
class stack:
    def __int__(self):
       self.items=[]
    def is_empty(self):
        return self.item==[]
    def push(self,x):
        self.item.append(x)
        print(self.items)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
s=stack()
print(s.is_empty())
s.push(10)
s.push(20)
print("peek",s.peek())
print("pop")
print(s.pop())
print(s.pop())
print("size of the stack;", s.size())
end=time.time()
print("run time of the bprogram is :",end-start)
