#list
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
#print("The Elements in Stack after appending: ",stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
#print("The Elements in Stacks after removing: ",stack)

#Implementation using collections.deque
from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print("The Elements in Stack after appending: ",stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("The Elements in Stacks after removing: ",stack)

#Implementation using queue module
from queue import LifoQueue
stack = LifoQueue(maxsize=3)
print(stack.qsize())

stack.put(1)
stack.put(2)
stack.put(3)
print(stack.full())
print(stack.qsize())

print(stack.get(2))
print(stack.full())
print(stack.qsize())

for elements in stack.queue:
    print(elements)








