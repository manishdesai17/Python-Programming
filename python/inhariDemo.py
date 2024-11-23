class student:
    def __init__(self,name,mobile,address):
        self.name=name
        self.mobile=mobile
        self.address=address

class marks(student):
    def __init__(self, name, mobile, address,sub1,sub2):
        super().__init__(name, mobile, address)
        self.sub1=sub1
        self.sub2=sub2

    def print(self):
        print("name=",self.name)
        print("mobile=",self.mobile)
        print("address=",self.address,)
        total=self.sub1+self.sub2
        print("Total=",total)
        print("percentage=",total/2)
    
mp=marks("manish",9089674523,"varnoda,deesa",50,60)
mp.print()


