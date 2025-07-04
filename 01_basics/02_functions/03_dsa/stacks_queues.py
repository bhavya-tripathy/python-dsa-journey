# stacks_queues.py - Using list as stack and queue

# Stack (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack:", stack)
stack.pop()
print("After popping:", stack)

# Queue (FIFO)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue:", queue)
queue.popleft()
print("After dequeuing:", queue)
