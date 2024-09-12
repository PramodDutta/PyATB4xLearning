# deque - double-ended queue
# FIFO - bus stand queue, airport queue
# A list-like sequence optimized for data accesses near its endpoints.

from collections import deque

# create a deque
# d = deque()
d = deque([1, 2, 3])
print(d)

d.append(4) # Item
print(d)

# Add an element to the left end
d.appendleft(0)
print(d)

# Extend(list) the deque
d.extend([5,6])
print(d)

print(d.pop()) # End
print(d.popleft())  # Start

d.reverse()
print(d)


