class MakeMyTrip:
    def search(self,destinaiton,checkinDate,checkOutDate,noOfppl,room):
        print('Hotels dispalyed!!')
    
    @classmethod
    def checkOut(cls,hotelName):
        print(f"room selected and checkedout in {hotelName}")
    
    @staticmethod
    def makePayment(paymentType):
        print(f"Payment successful via {paymentType}")
        
mmt = MakeMyTrip()
mmt.search(1,2,3,4,5)    
MakeMyTrip.checkOut('La Palooza')
MakeMyTrip.makePayment('UPI')