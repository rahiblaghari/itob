value= int(input("What number do you want to convert to binary: "))
def itob(x):
    return bin(x)[2:]
print(itob(value))