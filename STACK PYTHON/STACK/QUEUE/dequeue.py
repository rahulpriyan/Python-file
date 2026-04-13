queue=[10,20,30]
if len(queue)==0:
    print("queue underflow! cannot dequeue")
else:
    removed=queue.pop(0)
    print("dequeued element:",removed)
print("queue after dequeue:",queue)