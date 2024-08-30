'''
rock=1
scissor=-1
paper=0
'''
import random


computer=random.randint(-1,1)
youstr=input("Enter your a choice : ")
dict={ "r":1 ,"s":-1,"p":0 }
reversedict={1:"rock",-1:"scissor",0:"paper"}
you=dict[youstr]

print(f"you choose {reversedict[you]}")
print(f"computer choose {reversedict[computer]}")


if(computer==you):
    print("its a draw")
else:
    if(computer==-1 and you==1):
        print("YOU WON")
    elif(computer==-1 and you==0):
        print("YOU LOSE")
    elif(computer==1 and you==0):
        print("YOU WON")
    elif(computer==1 and you==-1):
        print("YOU LOSE")
    elif(computer==0 and you==-1):
        print("YOU WON")
    elif(computer==0 and you==1):
        print("YOU LOSE")
    else:
        print("something went wrong")


# # alternate method
# if(computer==you):
#     print("its a draw")
# else:
#     if((computer-you)==1 or (computer-you)==-2 ):
#         print("YOU WON")
#     else:
#         print("YOU LOSE")




