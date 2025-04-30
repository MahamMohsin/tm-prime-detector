from collections import defaultdict

class TuringMachine:
    def __init__(self, number):
        self.input_number = number
        self.tape = defaultdict(lambda: ' ')  #Infinite tape both directions
        self.head = 0
        self.state = 'START'
        self.divisor = 2  
        self.max_divisor = number - 1

        #Writing unary number on tape (e.g., 3 → 111)
        for i in range(number):
            self.tape[i] = '1'

    def reset_tape(self):
        self.tape = defaultdict(lambda: ' ')
        for i in range(self.input_number):
            self.tape[i] = '1'
        self.head = 0

    def simulate_division(self, divisor):
            """Simulates division by marking groups of cells as 'X'. Returns True if divisible."""
            tape_copy = dict(self.tape)
            pointer = 0
            count = 0
            step = 1  #For logging steps

            print(f"  Trying to divide unary by {divisor}")
            while pointer < self.input_number:
                group = 0
                indices = []
                while group < divisor and pointer < self.input_number:
                    if tape_copy.get(pointer, ' ') == '1':
                        indices.append(pointer)
                        group += 1
                    pointer += 1

                if group != divisor:
                    print("   Incomplete group found. Not divisible.")
                    return False

                #Mark the grouped cells
                for i in indices:
                    tape_copy[i] = 'X'

                #Print tape snapshot after marking each group
                tape_visual = ''.join(tape_copy.get(i, ' ') for i in range(self.input_number))
                print(f"   Step {step}: {tape_visual}")
                step += 1
                count += 1

            is_divisible = (count * divisor == self.input_number)
            print(f"   Final tape: {''.join(tape_copy.get(i, ' ') for i in range(self.input_number))}")
            return is_divisible


    def run(self):
        while self.state not in ['HALT_YES', 'HALT_NO']:
            if self.state == 'START':
                print(f"\n[STATE: {self.state}] Starting test for input: {'1' * self.input_number}")
                if self.input_number < 2:
                    self.state = 'HALT_NO'
                else:
                    self.state = 'CHECK_DIV'

            elif self.state == 'CHECK_DIV':
                print(f"\n[STATE: {self.state}] Testing divisor {self.divisor}...")
                if self.divisor > self.max_divisor:
                    self.state = 'HALT_YES'
                elif self.simulate_division(self.divisor):
                    print(f"  → Divisible by {self.divisor}: REJECT")
                    self.state = 'HALT_NO'
                else:
                    print(f"  → Not divisible by {self.divisor}, trying next...\n")
                    self.divisor += 1

        if self.state == 'HALT_YES':
            print("\n✅ Result: YES — Prime Number")
        else:
            print("\n❌ Result: NO — Not a Prime Number")
        return self.state == 'HALT_YES'


# ----------------------
def is_prime_tm(n):
    tm = TuringMachine(n)
    return tm.run()

# ------------------------------
def main():
    try:
        num = int(input("Enter a number to check if it's prime: "))
        if is_prime_tm(num):
            print(f"{num} is a Prime Number ✅")
        else:
            print(f"{num} is NOT a Prime Number ❌")
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
