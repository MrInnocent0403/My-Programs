name = str(input("Enter Your name: "))
print(f"Hello  {name}")
data = int(input(f"{name} Enter star count: "))
print(f"you select {data}")
dev=input("Enter Char to devide the stars: ")
def print_num_star(data):
    global dev
    for star in range(data):
        for m_star in range(star + 1):
                out = "*"
                print(out,end="")
                if m_star < star:
                  print(dev, end="")
                else:
                     break            
        print()
print_num_star(data)