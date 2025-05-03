from fooditem import Fooditem
from manue import Manue
from order import Order
from restuarent import Restuarent
from user import Customer,Admin,Employee

Kashmeri_dhaba=Restuarent("Kashmeri_dhaba")

def customer_manue():
    name=input("Enter your name: ")
    phone=input("Enter your phone no: ")
    email=input("Enter your email: ")
    address=input("Enter your address: ")

    customer=Customer(name=name,phone=phone,email=email,address=address)
    
    while True:
        print(f"Wellcome {customer.name}")
        print("1: View manue")
        print("2: Add item to cart")
        print("3: View cart")
        print("4: Pay bill")
        print("5: Exit")

        option=int(input("Enter option: "))
        if option==1:
            customer.view_manue(Kashmeri_dhaba)
        elif option==2:
            item_name=input("Enter item: ")
            item_quantity=int(input("Enter quantity: "))
            customer.add_to_cart(Kashmeri_dhaba,item_name,item_quantity)
        elif option==3:
            customer.view_cart()
        elif option==4:
            customer.pay_bill()
        elif option==5:
            break
        else:
            print("Invalid option")

    
def admin_manue():
    name=input("Enter your name: ")
    phone=input("Enter your phone no: ")
    email=input("Enter your email: ")
    address=input("Enter your address: ")

    admin=Admin(name=name,phone=phone,email=email,address=address)
    
    while True:
        print(f"Wellcome {admin.name}")
        print("1: Add new item")
        print("2: Add new employee")
        print("3: View employee")
        print("4: View item")
        print("5: Delete item")
        print("6: Exit")

        option=int(input("Enter option: "))
        if option==1:
            item_name=input("Enter item name: ")
            item_price=int(input("Enter item price: "))
            item_quantity=int(input("Enter quantity: "))
            item=Fooditem(item_name,item_price,item_quantity)
            admin.add_new_item(Kashmeri_dhaba,item)

        elif option==2:
            name=input("Enter employee name: ")
            phone=int(input("Enter employee phone: "))
            email=input("Enter employee email: ")
            address=input("Enter employee adress: ")
            age=int(input("Enter employee age: "))
            salary=int(input("Enter employee salary: "))
            designation=input("Enter employee designation: ")
            employe=Employee(name=name,phone=phone,email=email,address=address,age=age,salary=salary,designation=designation)
            admin.add_employe(Kashmeri_dhaba,employe)

        elif option==3:
            admin.view_employe(Kashmeri_dhaba)

        elif option==4:
            admin.view_manue(Kashmeri_dhaba)

        elif option==5:
            item_name=input("Enter item: ")
            admin.remove_item(Kashmeri_dhaba,item_name)

        elif option==6:
            break
        else:
            print("Invalid option")

while True:
    print("Wellcome!!")
    print("1: Customer")
    print("2: Admin")
    print("3: Exit")

    option=int(input("Enter option: "))
    if option==1:
        customer_manue()
    elif option==2:
        admin_manue()
    elif option==3:
        break
    else:
        print("invalid option")