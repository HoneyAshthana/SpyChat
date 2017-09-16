from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends
import re
from colorama import init,Fore

init()
image_pattern="^[a-zA-Z0-9]+.jpg$"

def read_message():
    # choose friend from the list
    sender = select_friend()

    if (sender == -1):
        print Fore.RED + "Wrong Choice" + Fore.RESET
    else:
        friends[sender].avgChatWords()
        while (True):
            encrypted_image = raw_input("Please provide the encryted image to decode")
            if re.match(image_pattern, encrypted_image, flags=0) is not None:
                break
            else:
                print Fore.RED + "Image name must be alpha numeric and image extension must be .jpg" + Fore.RESET
        try:
            secret_message = Steganography.decode(encrypted_image)
            print "The secret message is: " + secret_message
            #saves the messages
            new_chat = {
                "message": secret_message,
                "time": datetime.now(),
                "sent_by_me": False
            }
            friends[sender].get_chats().append(new_chat)
            print Fore.GREEN + "Message saved"
        except:
            print Fore.RED + "Sry either image is not available or the image does not contain any valid message" + Fore.RESET


