def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(start, end):
    if start < 1:
        print("Please enter a non-negative number.")
        return

    if end < start:
        print(f"Enter a number greater than {start}.")
        return

    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")


if __name__ == "__main__":
    while True:
        start = int(input("Enter a number (start): "))

        if start < 0:
            print("Please enter a non-negative number.")
            continue

        if start == 0:
            print("Program terminated.")
            break

        end = int(input("Enter a number (end): "))

        if end < start:
            print(f"Enter a number greater than {start}.")
        else:
            display_primes(start, end)
            print("\n")
