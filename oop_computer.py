class Computer:
    count_instance = 0
    def __init__(self, Name, Brand, Processor, HDD):
        Computer.count_instance+=1
        print("init")
        self.name = Name
        self.brand = Brand
        self.Processor = Processor
        self.HDD = HDD

Comp1 = Computer ("Apple Macbook Air", "Apple", "Intel i5", "500GB")
Comp2 = Computer ("Asus Vivobook", "Asus", "Intel i5", "1TB")
Comp3 = Computer ("Lenovo Thinkbook", "Lenovo", "Intel i5", "1TB")

print(id(Comp1))
print(Computer.count_instance)
print(Comp3.name)