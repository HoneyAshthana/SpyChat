# default user details
from steganography.steganography import Steganography

class Spy:
    def __init__(self,name,salutation,age,rating):

        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.is_online = True
        self.chat=[]

    def avgChatWords(self):
        #to calculate avg words in chats
        avg=0
        if len(self.chat)!=0:
            for i in self.chat:
                avg+=len(Steganography.decode(i['message']))
            avg=avg/len(self.chat)
            print "Average words : ",avg

    def displayDetails(self):
        print self.name, " ", self.age , " ", self.rating