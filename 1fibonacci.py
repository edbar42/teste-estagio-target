def is_fibonacci(n):
    if n < 1:
        return False

    a, b = 1, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b

    return False


if __name__ == "__main__":
    num = int(input("Digite um número: "))
    if is_fibonacci(num):
        print(f"{num} pertence à sequência Fibonacci.")
    else:
        print(f"{num} não pertence à sequência Fibonacci.")
