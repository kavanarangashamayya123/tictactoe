lst=[0,0,"X",0,"0",0,0,0,0]
def board():
    count=0
    for i in range(3):
        for j in range(3):
            if lst[count]==0:
                print(" __ | ",end="")
            else:
                print(lst[count]+" | ",end="")
            count+=1
        print()
board()
user="X"
game=True
def swap_users():
        if globals()['user']=="X":
            globals()['user']="0"
        else:
            globals()['user']="X"
def win(lst):
        if lst[0]=="X" and lst[1]=="0" and lst[2]=="X":
            globals()['games']=False
            print("X wins")
        
while game:
            n=int(input("enter the selection : "))
            lst[n-1]=user
            board()
            win(lst)
            
