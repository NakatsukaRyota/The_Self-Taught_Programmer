class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last= len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)
    

lists = [1, 2, 3, 4, 5]
reversed_lists = [] 

stack = Stack()
for num in lists:
    stack.push(num)

for i in range(0, stack.size()):
    reversed_lists.append(stack.pop())
print(reversed_lists)

