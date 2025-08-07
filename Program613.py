#Division
def Division(No1,No2):
    Ans = 0
    Ans = No1//No2    ## Floor Division // tyan javlcha answer miltey
    return Ans
    
   

def main():
    print("Enter First Number  : ")
    Value1 = int(input())

    print("Enter Second Number  : ")
    Value2 = int(input())


    iRet = Division(Value1,Value2)

    print(f"Division of {Value1} & {Value2} is {iRet} ")

if __name__ == "__main__":
    main()