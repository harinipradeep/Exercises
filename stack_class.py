class Stack:
    
    data = ["vd","hv","sv"]

    @classmethod
    def push(cls, x):
        cls.data.append(x)

    @classmethod
    def pop(cls):
        cls.data.pop()

    @staticmethod
    def display_stack():
       print(Stack.data)

Stack.display_stack()
Stack.push("ybv")
Stack.display_stack()
Stack.pop()
Stack.display_stack()

#$ python stack_class.py 
#['vd', 'hv', 'sv']
#['vd', 'hv', 'sv', 'ybv']
#['vd', 'hv', 'sv']

