#!/usr/bin/python3
# Define a Stack class
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


# Define the reverse function using a stack
def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


# Test the reverse_string function
string = "Javascript"
reversed_string = reverse_string(string)
print(f"The original string is: {string}")
print(f"The reversed string is: {reversed_string}")

