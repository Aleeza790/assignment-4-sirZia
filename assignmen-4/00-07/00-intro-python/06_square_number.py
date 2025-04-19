
def main():

    number = float(input("\033[1;3m Type a number to see it's square: \033[0m"))
    
    square = number * number
    
    print(f"{number} squared is {square}")



if __name__ == '__main__':
    main()