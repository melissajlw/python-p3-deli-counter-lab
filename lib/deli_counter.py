def line(deli):
    if len(deli) == 0:
        print("The line is currently empty.")
    else:
        tmp = "The line is currently:"
        for i in range(len(deli)):
            tmp += f" {i + 1}. {deli[i]}"
        print(tmp)
            

def take_a_number(deli, name):
    print(f"Welcome, {name}. You are number {len(deli) + 1} in line.")
    deli.append(name)

def now_serving(deli):
    if (len(deli) == 0):
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {deli[0]}.")
        del deli[0]