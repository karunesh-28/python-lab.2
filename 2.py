class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)

# Taking user input to perform operations on the stack
stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the element to push: ")
        stack.push(item)
        print(f"{item} pushed onto the stack.")
    elif choice == '2':
        popped_item = stack.pop()
        if popped_item is not None:
            print(f"Popped item: {popped_item}")
    elif choice == '3':
        peeked_item = stack.peek()
        if peeked_item is not None:
            print(f"Peeked item: {peeked_item}")
    elif choice == '4':
        print(f"Stack size: {stack.size()}")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
