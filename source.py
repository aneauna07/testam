class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

def findInStack(stack, x):
   
    # Implementējiet funkciju, kas atgriež True, ja elements 'x' atrodas kaudzē, pretējā gadījumā False.
    # Jūsu kods šeit.

    return found

def loadValuesFromFile(filename, stack):
    try:
        with open(filename, 'r') as file:
            values = file.readline().split() 
            for value in values:
                stack.push(int(value))  
    except FileNotFoundError:
        print(f"Failu '{filename}' nevar atrast.")



myStack = Stack()
filename = "values.txt"  
loadValuesFromFile(filename, myStack)


elementToFind = 1
isElementFound = findInStack(myStack, elementToFind)
print(isElementFound)
