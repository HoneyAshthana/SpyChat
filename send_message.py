from select_friend import select_friend
from steganography.steganography import Steganography

def send_message():
    #function logic
    friend_choice = select_friend()

    #prepare the  message
    original_image = raw_input("Provide the name of the image to hide the message")
    output_image = raw_input("Provide the name of the output image : ")
    text = raw_input("Enter your message here : ")
    #Encrypt the message
    Steganography.encode(original_image,output_image,text)

    #Successful message
    print "Your mesasge  encrpyted successfully"