from dataclasses import dataclass
@dataclass
class Stek():
 stack=list()
 def push(self,item):
        self.stack.append(item)
 def pop(self):
        return self.stack.pop()
Stek1=Stek()
Stek1.push(2)
Stek1.push(7)
Stek1.push(13)
Stek1.push(22)
Stek1.push(33)
Stek1.push(41)
Stek1.pop()
Stek1.pop()
print('стек:',Stek1.stack)

