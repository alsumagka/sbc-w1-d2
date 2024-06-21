from random import randint

user = input("PLACE YOUR BET (e.g., '1 2 3'): ").split()
users = [int(x) for x in user]
result = [randint(0, 9) for _ in range(3)]

print(f"BET: {' '.join(map(str, users))}")
print(f"RESULT: {' '.join(map(str, result))}")

if user == result:
    print("You Win!")
elif sorted(users) == sorted(result):
    print("You partially win!")
else:
    print("You lose!")
