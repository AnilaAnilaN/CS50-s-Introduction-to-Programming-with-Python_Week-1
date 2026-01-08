greeting = input("If you don't greet with a Hello, you'll be charged $100! ")

greeting = greeting.strip()


if greeting.startswith("Hello") or greeting.startswith("hello"):
    print("$0")
elif (greeting.startswith("H") or greeting.startswith("h")) and not((greeting.startswith("Hello")) or greeting.startswith("hello")):
    print("$20")
else:
    print("$100")
