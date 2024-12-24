with open("numbers.txt","w") as file:
    for number in range(101):
        file.write(f"{number}\n")
print("numbers from 0 to 100 in file 'numbers.txt' ")


filename = input("input your text fime name: ")
try:
    with open(filename, "r") as file:
        content = file.read()
    print("in your file: ")
    print(content)
except FileNotFound:
    print(f"file '{filename}' is not found")


input_image = input("insert file name with image: ")
try:
    with open(input_image, "rb") as source:
        data = source.read()
    with open("1.png", "wb") as destnation:
        print("data from image write into file '1.png'")
except FileNotFound:
    print(f"file '{input_image}' is not found")
