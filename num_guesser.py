while True:
    try:
        i = 0
        c = int(input("How Many Guess Do You want: "))
        print("What Should Be The Range ")
        h = int(input("1 no. "))
        g = int(input("2 no. "))
        print("Total Guess = " , (c))
        print("Make Your Guess Between" ,(h), " to ", (g))

        
        
        import random
        x = random.randint((h),(g))
##      print(x)
        while i < c:
            e  = int(input("Make Your Guess "))  
            if e == (x):
                print("you Win")
                break
            elif e < (x):
                    print("Too short ")
                    c-=1
                    print("Total guess left:",c)
            elif e > (x):
                print("Too big ")
                c-=1
                print("Total guess left:",c)
                
        else:
            print("You lose\n*************************************")
    except ValueError:
        print("Please Enter Valid Value ")
