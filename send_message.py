from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends
from colorama import init,Fore
import re
init()
image_pattern="^[a-zA-Z0-9]+.jpg$"
name_pattern="^[a-zA-Z]+[\sa-zA-Z]*$"

def send_message():
    #function logic of choosing friend from the list

    friend_choice = select_friend()
    if friend_choice == -1:
        print Fore.RED + "wrong choice"
    else:
        friend_choice = (friend_choice)
        while True:
            original_image = raw_input("Provide name of image to hide message : ")
            if re.match(image_pattern, original_image, flags=0) is not None:
                break
            else:
                print Fore.RED + "Image name must be alpha numeric and image extension must be .jpg"
        while True:
            output_image = raw_input("Provide the name of output image : ")
            if re.match(image_pattern, output_image, flags=0) is not None:
                break
            else:
                print Fore.RED + "Image name must be alpha numeric and image extension must be .jpg" + Fore.RESET
        while True:
            text = raw_input("Enter your message : ")
            if (len(text) > 100):
                print Fore.RED+"Too large Message"
            elif len(text)<0:
                print Fore.RED + "Please provide some message. It cannot be empty." + Fore.RESET
            else:
                break
        try:
            Steganography.encode(original_image, output_image, text)
            print Fore.GREEN + "Message encrypted successfully"

            # Save the chats
            new_chat = {
                'message': output_image,
                'time': datetime.now(),
                'sentby': True
            }

            # saving the dictionary
            friends[friend_choice].chat.append(new_chat)
            print "Message saved successfully" + Fore.RESET

        except IOError:
            print Fore.RED + "NO such image exist in the module."