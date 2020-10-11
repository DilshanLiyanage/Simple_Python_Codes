class Test1:
    __name = ""
    __address = ""

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def set_name (self, name):
        self.__name = name

    def set_address (self, address):
        self.__address = address

    def get_name (self):
        return self.__name

    def get_address (self):
        return  self.__address


test1 = Test1("Dilshan", "Galle, Sri lanka")
print ("Default name "+ test1.get_name())
print ("Default address "+ test1.get_address())
test1.set_name("Tharusha")
test1.set_address("Matara, Sri Lanka")
print ("Changed name "+ test1.get_name())
print ("Changed address "+ test1.get_address())