from dataclasses import dataclass
@dataclass
class Stek():
 stack=list()
 def push(self,item):
        self.stack.append(item)
 def pop(self):
        return self.stack.pop()
Stek1=Stek()
Stek1.push(4)
Stek1.push(7)
Stek1.push(12)
Stek1.push(15)
Stek1.push(21)
Stek1.pop()
print('стек:',Stek1.stack)

