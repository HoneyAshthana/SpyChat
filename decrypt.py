from steganography.steganography import Steganography



def read_message():
    # choose friend from the list

    encrypted_image = raw_input("Provide encrypted image : ")
    secret_message = Steganography.decode(encrypted_image)
    print secret_message



