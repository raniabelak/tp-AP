

msg=str(input("please type a string: "))
while(msg!=""):
    print("\033[4m",msg,"\033[0m")
    msg=str(input("please type a string: "))
    
# code for starting underlining is: \033[4m
# code for ending underlining is: \033[0m