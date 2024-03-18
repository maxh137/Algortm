from dataclasses import dataclass
@dataclass
class Stek():
 stack=list()
 def push(self,item):
        self.stack.append(item)
 def pop(self):
        return self.stack.pop()
Stek1=Stek()
Stek1.push(1)
Stek1.push(3)
Stek1.push(10)
Stek1.push(15)
Stek1.push(22)
Stek1.pop()
print(Stek1.stack)
