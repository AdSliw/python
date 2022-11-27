class DeltaFunction:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.x = str('x')

    def print_function(self):
        print("Function is: ", self.a, '*', self.x, '^2', '+', self.b, '*', self.x, '+', self.c)

    def calculate_delta(self):
        delta = int(self.b) ** 2 - 4 * int(self.a) * int(self.c)
        print('Delta equals: ', str(self.b), '^2 - 4 *', str(self.a), '*', str(self.c), '=', delta)


value1 = 3
value2 = 4
value3 = 1

function = DeltaFunction(value1, value2, value3)
function.print_function()
function.calculate_delta()
