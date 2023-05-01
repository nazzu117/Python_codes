class Gfather:
    age=77
    name="karakarakara"
    city="Hyderabad"
    GDP=10
    year=2020
    def Gfat(self):

        return "{} is {} of {}".format(self.age,self.name,self.GDP)

class father():
    name="Samaram"
    age=55
    s_name="kamathi"
    in_cm=100000000
    city="Banglore"
    def chld(self):

        return " {} age is {} he has a {} anual income ".format(self.name,self.age,self.in_cm)

    
class children(father,Gfather):
    name="sumabara"
    age=25
    qulf="Doctor"
    def chld(self):

        return "{} age is {} he is a {} ".format(self.name,self.GDP,self.qulf)

fam=children()

print(fam.city)
print(fam.qulf)
print(fam.chld())

