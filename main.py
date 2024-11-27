from PIL import Image

colors_list = []

imgpath = input("Enter the image path > ")

print("1. Sort One")
print("2. Sort One Reverse")
print("3. Sort Two")
print("4. Sort Two Reverse")
method = input("Select a method > ")

img = Image.open(imgpath)

width, height = img.size

def sort_one():
    for x in range(width):
        line = []
        for y in range(height):
            line.append(img.getpixel((x,y)))
    
        colors_list.append(sorted(line))

def sort_two():
    for x in range(width):
        line = []
        for y in range(height):
            line.append(img.getpixel((x,y)))
    
        colors_list.append(line)

    colors_list.sort()

def sort_one_reversed():
    for x in range(width):
        line = []
        for y in range(height):
            line.append(img.getpixel((x,y)))
    
        colors_list.append(sorted(line, reverse=True))

def sort_two_reversed():
    for x in range(width):
        line = []
        for y in range(height):
            line.append(img.getpixel((x,y)))
    
        colors_list.append(line)

    colors_list.sort(reverse=True)

match method:
    case "1":
        sort_one()
    case "2":
        sort_one_reversed()
    case "3":
        sort_two()
    case "4":
        sort_two_reversed()
    case _:
        print("Invalid method")
        exit()

new = Image.new("RGB", (width, height))

# Display
for x in range(width):
    for y in range(height):
        new.putpixel((x,y), colors_list[x][y])

new.show()