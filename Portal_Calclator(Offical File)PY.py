import json
import math

print("=======================")
print("Portal Calculator 5.4 🧮")
print("=======================")

#File
HISTORYFILE = "history.json"
AREAFILE = "area.json"
NUMBERFILE = "numbers.json"

#LOAD HISTORY
def load_history(HistoryFile):
    with open(HistoryFile, "a") as file:
        pass
    with open(HistoryFile, "r") as file:
        Content = file.read()
        if Content.strip() != "":
            return json.loads(Content)
        return []

#SAVE HISTORY
def save_history(HistoryFile, Data):
    with open(HistoryFile, "w") as file:
        json.dump(Data, file)

#COLCULATOR
def calculator():
    history = load_history(HISTORYFILE)
    while True:
        Opera = input("\nChoose an (+ , - , * , / , ** , % , √(sqrt)) , R" "\nInput R for Return to main meniu \n>>").strip().lower()
        if Opera == "√" or Opera == "sqrt":
            sqrt()
            continue
        if Opera == "r":
            print("Calculator has closet.")
            save_history(HISTORYFILE, history)
            if history:
                print("\n ---Calculation History---")
                history.sort()
                for item in history:
                    print(item)
                    print("-----------------------")
            else:
                print("No History.")
            return
        if Opera not in ["+" , "-" , "*" , "/" , "**" , "%" , "√" , "sqrt" ]: 
            print("⛔ Error: Invalid operation!")
            continue 
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter secend number: "))
        if Opera == "+" :
            Result= num1 + num2
            print(f"{num1} + {num2} = {Result}")
        elif Opera == "-" :
            Result= num1 - num2
            print(f"{num1} - {num2} = {Result}")
        elif Opera == "**": 
            Result = num1 ** num2
            print(f"{num1} ** {num2} = {Result}")
        elif Opera == "*":
            Result= num1 * num2
            print(f"{num1} * {num2} = {Result}")
        elif Opera == "%":
            if num2 !=0 :
                Result= num1 % num2
                print(f"{num1} % {num2} = {Result}")
            else :
                print("⛔ Error: Cannot divide by zero!")
        elif Opera == "/":
            if num2 !=0:
                Result= num1 / num2
                print(f"{num1} / {num2} = {Result}")
            else:
                print("⛔ Error: Cannot divide by zero!")
        history.append(f"{num1} {Opera} {num2} = {Result}")

#AREA
def area():     
    print("\n--Area of geometric shapes--")
    area_history = load_history(AREAFILE)
    Sq_list = []
    Ci_list = []
    Tr_list = []
    while True:
        print("(S): Square" , "(C): Circle" , "(T)Triangle" , "(R)Return to main meniu")
        shape = input().strip().lower()
        if shape == "s":
            side = float(input("Side length: "))
            area = side * side
            Sq_list.append(f"Squre({side}) = {area}")
        elif shape == "c":
            r = float(input("Redius: "))
            area= 3.145 * r **2
            Ci_list.append(f"Circle({r}) = {area}")
        elif shape =="t":
            base = float(input("Base: "))
            height = float(input("Height: "))
            area = 0.5*height*base
            Tr_list.append(f"Triangle({height}) = {area}")
        elif shape == "r":
                print("Return to main meniu>>>>>>>")
                print(f"Squres:{Sq_list}")
                print(f"Circles:{Ci_list}")
                print(f"Triangles:{Tr_list}")
                save_history(AREAFILE, area_history)
                break
        else:
            print("⛔ Error: Invalid operation!")
        print(f"Area:{area}")

#COMPOSITE & PRIME NUMBERS
def composite_prime():
    print("--Composite & Prime numbers--")
    number_history = load_history(NUMBERFILE)
    while True:
        Input = input("Enter a number (Maximum limit) or Enter (R) for return to main meniu:") 
        if Input == "r":
            print("Return to main meniu>>")
            save_history(NUMBERFILE, number_history)
            break
        if Input.isdigit() == False :
            print("⛔ Error: Invalid operation!")
            continue
        limit = int(Input)
        if limit < 2:
            print("⛔Liminited must be up to 2")
            continue
        Comp_list = []
        Prim_list = []
        for num in range(2, limit + 1 ):
            Prime = True
            for i in range(2, int(math.sqrt(num)) +1):
                if num % i ==0 :
                    Prime = False 
                    break
            if Prime == False:
                Comp_list.append(num)
            else:
                Prim_list.append(num)
        Comp_list.sort()
        Prim_list.sort()
        print("Composit Number: ")
        for c in Comp_list:
            print(c)
        print("\n")
        print("Prime Number :")
        for p in Prim_list:
            print(p)
        print("\n")
        number_history.append({"limit": limit, "Prime": Prim_list, "Composites": Comp_list})

#SQRT
def sqrt():
    num = float(input("Enter a number: "))
    result = math.sqrt(num)
    print(f"√{num} = {result}")
    history = load_history(HISTORYFILE)
    history.append(f"√{num} = {result}")
    history.append(f"√{num} = {result}")

#SHOW HISTORY
def ShowAllHistory():
    print("\n.......All History......")
    print("\n.......Calculator Hitory .....")
    calc_history = load_history(HISTORYFILE)
    if calc_history:
        for item in calc_history:
            print(item)
    else:
        print("No History>>")
    print("\n......Area History........")
    area_history = load_history(AREAFILE)
    if area_history:
        for item in area_history:
            print(item)
    else:
        print("No History>>")
    print("\n......Numbers Hisoty........")
    number_history = load_history(NUMBERFILE)
    if number_history:
        for item in number_history:
            if type(item) == dict:
                limit = item.get("limit", "?")
                primes = item.get("primes", [])
                composites = item.get("composites", [])
                print(f"Limit: {limit}")
                print(f"Primes: {primes}")
                print(f"Composites: {composites}")
                print("-----------------------")
            else:
                print(item)
    else:
        print("No History>>")
    print("\n.............................................")
    
    
#MAIN MENU
while True:
    print("\n--Main Menu--")
    print("1. Calculator")
    print("2. Area of geometric shapes")
    print("3. Composite & Prime numbers")
    print("4. History ")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        calculator()
    elif choice == "2":
        area()
    elif choice == "3":
        composite_prime()
    elif choice == "4":
        ShowAllHistory()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("⛔ Error: Invalid choice! Please enter a number between 1 and 5.")

    