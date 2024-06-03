from dataclasses import dataclass
@dataclass
class Stek():
 stack=list()
 def push(self,item):
        self.stack.append(item)
 def pop(self):
        return self.stack.pop()
Stek1=Stek()
Stek1.push(11)
Stek1.push(20)
Stek1.push(53)
Stek1.push(27)
Stek1.push(38)
Stek1.push(67)
Stek1.pop()
Stek1.pop()
print('стек:',Stek1.stack)

