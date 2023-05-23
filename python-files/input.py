class InputHandler():
    def __init__(self):
        self.input = None

    def get_input(self):
        self.input = input("Enter a number: ")
        return self.input

    def print_input(self):
        print(self.input)