#Getting the queue ready
queue = []

#Adding three items to the end
queue.append("a")
queue.append("b")
queue.append("c")

#Removing from position 0, (the front)
print("Inital Queue")
print(queue.pop(0))
print(queue.pop(0))

#Printing the queue
print("\nQueue after removing elements")
print(queue)

#Peak
print("peak:")
print(queue[0])
