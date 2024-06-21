from random import randint

user = input("FOLD OR UNFOLD? ").upper()
print(f"USER: {user}")

C2 = "FOLD" if randint(1, 2) == 1 else "UNFOLD"
print(f"C2: {C2}")

C3 = "FOLD" if randint(1, 2) == 1 else "UNFOLD"
print(f"C3: {C3}")

if user == C2 == C3:
    print("DRAW")
elif user == C2 and user != C3:
    print("C3 wins")
elif user != C2 and user == C3:
    print("C2 wins")
else:
    print("User wins")
