from random import randint

class Train:
    
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        
    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")
    
    def get_status(slf):
        print(f"Train no: {slf.trainNo} is running on time")
    
    def get_fare(slf, fro, to):
            print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(100, 5000)}")
        
t = Train(12355)
t.book("Delhi" , "Banaras")
t.get_status()
t.get_fare("Delhi" , "Banaras")
    
    
    