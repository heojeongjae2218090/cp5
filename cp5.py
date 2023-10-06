def print_구구단(n):
    for x in range(1, n+1):
        print(f"-------[ {x} 단] -------")
        for y in range(1, n+1):
            print(f"{x} x {y} = {x*y}")

num = input("몇 단까지 출력할까요? ")
num = int(num)
print_구구단(num)
