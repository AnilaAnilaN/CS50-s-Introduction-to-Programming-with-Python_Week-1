
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?  ")

#removing any extra spaces before and after the value user inputs and converting it to lowercase to deal with case sensitivity
answer = answer.strip().lower()

match(answer):
    case "forty two" | "forty-two" | "42":
        print("Yes")
    case _:
        print("No")
