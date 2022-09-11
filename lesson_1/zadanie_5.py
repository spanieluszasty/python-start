if __name__ == "__main__":
    for i in range(0, 101):
        if i % 15 == 0:
            print(i, "FizzBuzz")
        elif i % 5 == 0:
            print(i, "Buzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        else:
            print(i)
