# start printing 
def Display(No):
    i = 1
    while i <= No :
        print("*")
        i = i + 1
    
def main():
    print("Enter Number : ")
    Value =int(input())


    
    Display(Value)


if __name__ == "__main__":
    main()