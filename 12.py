'''Define a class with a generator which can iterate the numbers, which are divisible
by 7, between a given range 0 and n.'''

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_numbers(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Example usage:
n = int(input("Enter the value of n: "))
divisible_by_seven_generator = DivisibleBySeven(n).generate_numbers()

print(f"Numbers divisible by 7 between 0 and {n}:")
for number in divisible_by_seven_generator:
    print(number)
