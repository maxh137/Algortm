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
Ochered1.enqueue(2)
Ochered1.enqueue(11)
Ochered1.enqueue(23)
Ochered1.enqueue(77)
Ochered1.enqueue(85)
Ochered1.enqueue(92)
Ochered1.dequeue()
print('очередь:',Ochered1.queue)

