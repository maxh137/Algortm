class Ochered():
 def __init__(self):
  self.queue=[]
 def enqueue(self,item):
  self.queue.append(item)
 def dequeue(self):
     return self.queue.pop(0)
 def size(self):
     return len(self.queue)
Ochered1=Ochered()
Ochered1.enqueue(1)
Ochered1.enqueue(17)
Ochered1.enqueue(32)
Ochered1.enqueue(43)
Ochered1.enqueue(51)
Ochered1.dequeue()
print(Ochered1.queue)

