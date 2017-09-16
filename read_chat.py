from select_friend import select_friend
from globals import friends
from steganography.steganography import Steganography
from colorama import init,Fore

init()

def read_chat():
    # choose friend from the list
    friend_choice = select_friend()
    if friend_choice == -1:
        print Fore.RED + "Wrong choice,List empty" + Fore.RESET
    else:
        print (Fore.GREEN + "Messages sent by you is shown in green color \n" + Fore.RED + "Messages received and read by your friend is shown in red color:" + Fore.RESET)
        spybob=friends[friend_choice]
        spybob.avgChatWords()
        #to check chat is empty or not
        if len(spybob.chat)>0:
            for encrypted_image in spybob.chat:
                encrypted_image = raw_input("Provide encrypted image : ")
                encrypted_image.message=Steganography.decode(encrypted_image)
        else:
            print Fore.RED+"Presently no chat history"



