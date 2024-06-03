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
Ochered1.enqueue(12)
Ochered1.enqueue(22)
Ochered1.enqueue(43)
Ochered1.enqueue(67)
Ochered1.enqueue(81)
Ochered1.dequeue()
Ochered1.dequeue()
print('очередь:',Ochered1.queue)

