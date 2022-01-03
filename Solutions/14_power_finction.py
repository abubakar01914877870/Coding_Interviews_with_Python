if __name__ == "__main__":
    x = 2
    n = -3

    def power(x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / power(x, -n)
        if n % 2 == 1:
            return x * power(x, n - 1)
        a = power(x, n/2)
        return a * a

    print(power(x, n))
