from abc import ABC
from order import Order

class Users(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address


class Customer(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=Order()

    def view_manue(self,restuarent):
        restuarent.manue.show_manue()
    
    def add_to_cart(self,restuarent,item_name,quantity):
        item=restuarent.manue.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print("item quantity exceeded!!")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print("add to cart successfully")
        else:
            print("item not found")
    
    def view_cart(self):
        print("*******view cart*******")
        print("name\tprice\tquantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"total price: {self.cart.total_price()}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price()} paid successfully!!")
        self.cart.clear()       



class Employee(Users):
    def __init__(self, name, phone, email, address,age,salary,designation):
        super().__init__(name, phone, email, address)
        self.age=age
        self.salary=salary
        self.designation=designation




class Admin(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employe(self,restuarent,employe):
        restuarent.add_employe(employe)

    def view_employe(self,restuarent):
        restuarent.view_employe()
    
    def add_new_item(self,restuarent,item):
        restuarent.manue.add_item(item)

    def remove_item(self,restuarent,item):
        restuarent.manue.remove_item(item)
    
    def view_manue(self,restuarent):
        restuarent.manue.show_manue()
