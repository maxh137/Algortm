from dataclasses import dataclass
@dataclass
class Ochered():
  queue=list()
  def enqueue(self,item):
     return self.queue.append(item)
  def dequeue(self):
     return self.queue.pop(0)
  def size(self):
     return len(self.queue)
Ochered1=Ochered()
Ochered1.enqueue(17)
Ochered1.enqueue(10)
Ochered1.enqueue(43)
Ochered1.enqueue(59)
Ochered1.enqueue(61)
Ochered1.dequeue()
Ochered1.dequeue()
print('очередь:',Ochered1.queue)

