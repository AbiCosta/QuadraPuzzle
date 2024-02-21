#---Import the random module---
import random

#---creating variables---
start_point=""
user_name=""
user_input=0
user_list = []
replay=0
count=1
points=0
tot_points=0
randomlist= []

print("Please Use Full Screen while Running the Programme""\n")

while True:
    while True:
        start_point=input("Do You Want to Play the Game(YES or NO)? ")
        start_point=start_point.upper()
        if start_point=="YES":
            break
        elif start_point=="NO":
            exit()
        else:
            print("\n""Enter YES or NO \n")

    #---Getting Inputs---
    user_name=input("\n""Enter Your Name Please: ")
    print("".rjust(23),"Hi",user_name,"Welcome to GameInt")
    print("Number to Guess - XXXX".ljust(47),"Color Mapping:""\n".ljust(70),"1-White 2-Blue 3-Red""\n".ljust(76),"4-Yellow 5-Green 6-Purple")

    while True:
        print("".rjust(39),"\u0332".join("Attempt No").ljust(32),"\u0332".join("Guess").ljust(19),"\u0332".join("Result"))
        count = 1
        
        #Creating a random List
        randomlist=random.sample(range(1,6),4)
        
        while (count<=8):
            if count==9:
                break
            else:
                #---creating infinate while loop for get valid input---
                while True:
                    try:
                        user_input=int(input("Enter 4 Digit Number: "))
                        if len(str(user_input)) == 4:
                            break
                        elif user_input == 0000:
                            exit()
                        else:
                            print("\n""You Must Enter 4 Digit Number""\n")
                    except ValueError:
                        print("\n""You Must Enter 4 Integer""\n")

                #---converting user input into list---
                for num in range(4):
                    str_user_input = str(user_input)
                    user_list.append(str_user_input[num])

                for num in range(1):
                    if int(user_list[0])==randomlist[0] and int(user_list[1])==randomlist[1] and int(user_list[2])==randomlist[2] and int(user_list[3])==randomlist[3]:
                        print("".rjust(45),count,"".rjust(15),user_input,"".rjust(12),"1 1\n","".rjust(80),"1 1")
                        print("Congratulations !!!!! You have won the game...")
                        #---points allocation---
                        if count==1:
                            points=100

                        elif count==2:
                            points=50

                        elif count==3:
                            points=33

                        elif count==4:
                            points=25

                        elif count==5:
                            points=20

                        elif count==6:
                            points=16

                        elif count==7:
                            points=14

                        else:
                            points=12

                        tot_points+=points
                        print("You Have Scored",tot_points,"Points""\n")
                        count=10
                    else:
                        for i in range(1):
                            if int(user_list[0])>6 or int(user_list[1])>6 or int(user_list[2])>6 or int(user_list[3])>6 or int(user_list[0])<1 or int(user_list[1])<1 or int(user_list[2])<1 or int(user_list[3])<1:
                                print("You Should only Enter Input in Range 1 to 6")
                                user_list.clear()
                            else:
                                #---comparing user list with random list---
                                for num1 in range(1):
                                    if int(user_list[0])==randomlist[0]:
                                        print("".rjust(45),count,"".rjust(15),user_input,"".rjust(12),"1",end=" ")
                                    elif int(user_list[0])==randomlist[1] or int(user_list[0])==randomlist[2] or int(user_list[0])==randomlist[3]:
                                        print("".rjust(45),count,"".rjust(15),user_input,"".rjust(12),"0",end=" ")
                                    else:
                                        print("".rjust(45),count,"".rjust(15),user_input,"".rjust(12),".",end=" ")

                                for num2 in range(1):
                                    if int(user_list[1])==randomlist[1]:
                                        print("1")
                                    elif int(user_list[1])==randomlist[0] or int(user_list[1])==randomlist[2] or int(user_list[1])==randomlist[3]:
                                        print("0")
                                    else:
                                        print(".")
                                for num3 in range(1):
                                    if int(user_list[2])==randomlist[2]:
                                        print("".rjust(81),"1",end=" ")
                                    elif int(user_list[2])==randomlist[0] or int(user_list[2])==randomlist[1] or int(user_list[2])==randomlist[3]:
                                        print("".rjust(81),"0",end=" ")
                                    else:
                                        print("".rjust(81),".",end=" ")
                                for num4 in range(1):
                                    if int(user_list[3])==randomlist[3]:
                                        print("1")
                                    elif int(user_list[3])==randomlist[0] or int(user_list[3])==randomlist[1] or int(user_list[3])==randomlist[2]:
                                        print("0")
                                    else:
                                        print(".")
                                print("_______________________________________________________________________________________")
                                count=count+1
                    user_list.clear()


                    #---creating function for replay---
                    if (count==9):
                        print("You Lose the Game, You can only Guess 8 Times...")
                        #---creating infinate while loop for get valid input---
                        while True:
                            try:
                                replay=input("Do you want to play another game(Yes/No)? ")
                                replay= replay.upper()
                                if replay=="YES":
                                    print()
                                    print()
                                    break
                                elif replay=="NO":
                                    exit()
                                else:
                                    print("\t""Input Valid Input: Yes or No")
                            finally:
                                pass
                    elif (count==10):
                        #---creating infinate while loop for get valid input---
                        while True:
                            try:
                                replay=input("Do you want to play another game(Yes/No)? ")
                                replay= replay.upper()
                                if replay=="YES":
                                    print()
                                    print()
                                    break
                                elif replay=="NO":
                                    exit()
                                else:
                                    print("\t""Input Valid Input: Yes or No")
                            finally:
                                pass

