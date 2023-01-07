class Person:

    def __init__(self,name,last,age,pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay

    def pay_update(self,new_pay):
        self.pay = new_pay

p1 = Person("James","Bond",25,5000)

print(p1.pay)
p1.pay_update(2000)
print(p1.pay)

