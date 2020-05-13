import Cell,Charts

def main_func():
    try:
        print("Enter your Choice")
        print("1.Enter a new cell")
        print("2.Enter a chart")
        n = int(input('->'))
        filename = input("Enter your file name:")

        if n == 1:
            Cell.insert_cell(filename)
        elif n == 2:
            Charts.charts(filename)
            
    except FileNotFoundError:
        print("File Does not exist")
        print("Enter another file name")
        main_func()

main_func()
