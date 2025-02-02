import random 

n = random.randint(0, 100)

if n % 2 == 0:
    print(f"""O numero {n} é par!""")
else:
    print(f"O numero {n} é impar")