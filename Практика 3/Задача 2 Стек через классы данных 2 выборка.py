from dataclasses import dataclass
@dataclass
class Stek():
 stack=list()
 def push(self,item):
        self.stack.append(item)
 def pop(self):
        return self.stack.pop()
Stek1=Stek()
Stek1.push(6)
Stek1.push(9)
Stek1.push(10)
Stek1.push(15)
Stek1.push(23)
Stek1.push(31)
Stek1.pop()
print('стек:',Stek1.stack)

