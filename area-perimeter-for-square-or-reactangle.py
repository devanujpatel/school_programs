# input a number choice fom the user. if choice is square then input side and print area and perimeter if recatngle then input length nad breadth shoe area perimeter

choice = input("Enter s for square or r for rectangle: ")

if choice == 's':
    side = int(input("Enter side length for square: "))
    area = side*side
    perimeter = 4*side
    print("Area:",area,"perimeter:", perimeter)
else:
    # means choice is rectangle
    length = int(input("Length of rectangle: "))
    breadth = int(input("Breadth of rectangle: "))
    area = length*breadth
    perimeter = 2 * (length + breadth)
    print("Area:",area,"perimeter:", perimeter)
