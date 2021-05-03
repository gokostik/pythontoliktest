#print("привіт хресний")
#age = input("скільки тобі років?")
#print(f"о... {age}... то ти старий пердун...")
math = True
is_a_cool = False
is_b_cool = False

while math:


# ВВЕДЕННЯ А
    while not is_a_cool:
        try:
            A = float(input("введіть a=").replace(",","."))
            is_a_cool = True
        except:
            print("a має бути числом")

# ВВЕДЕННЯ Б
    while not is_b_cool:
        try:
            B = float(input("введіть B=").replace(",","."))
            is_b_cool = True
        except:
            print("B має бути числом")


    print(f"A-B={A-B}")
    print(f"A+B={A+B}")
    print(f"A*B={A*B}")
    try:
        print(f"A/B={A/B}")
    except:
        print("ділити на нуль не можна")


    is_a_cool = False
    is_b_cool = False
