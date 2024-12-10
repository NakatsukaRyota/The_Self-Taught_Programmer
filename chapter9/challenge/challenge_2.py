ans = input("あなたのわんこの名前は？: ")

with open("your_pet_name.txt", "w", encoding="utf-8") as f:
    f.write(ans)