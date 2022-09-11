if __name__ == "__main__":
    n = int(input("Podaj ile wierszy: "))
    ile_xow = 1
    for i in range(n):
        for j in range(ile_xow):
            print("x", end='')
        print()
        ile_xow += 2
