queue=[10,20,30]
if len(queue)==0:
    print("queue underflow! cannot enqueue")
else:
    added=queue.append(40)
    print("queued element:",added)
print("queue after enqueue:",queue)