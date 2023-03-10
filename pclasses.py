import csv
import os.path
import datetime

# Defining Pizza Superclass 
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

# Defining Pizza Subclasses
class Klasik(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 100.0)


class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita", 110.0)


class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza", 150.0)


class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 90.0)

class Newyork(Pizza): ##############
    def __init__(self):
        super().__init__("New York Pizza", 160.0)


class Italiano(Pizza):
    def __init__(self):
        super().__init__("Italiano Pizza", 160.0)


class Callypso(Pizza):
    def __init__(self):
        super().__init__("Callypso Pizza", 170.0)


class Konyalim(Pizza):
    def __init__(self):
        super().__init__("Konyalim Pizza", 180.0)

class Fourcheese(Pizza):
    def __init__(self):
        super().__init__("Four Cheese Pizza", 180.0)


class Ocakbasi(Pizza):
    def __init__(self):
        super().__init__("Ocakbasi Pizza", 180.0)

# The Decorator superclass was created to collect the fees of the 10 pizza subclasses and the fees of the sauces.
class Decorator:
    def __init__(self, component, pizza, extra_cost):
        self.component = component
        self.pizza = pizza
        self.extra_cost = extra_cost

    def get_cost(self):
        return self.extra_cost + self.pizza.get_cost()

    def get_description(self):
        return self.component + " Soslu " + self.pizza.get_description()

# Based on the Decorator superclass, 10 sauce subclasses with their own special extras were created.
class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__("Zeytin", pizza, 5.0)


class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__("Mantar", pizza, 7.0)


class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__("Keci Peyniri", pizza, 10.0)


class Et(Decorator):
    def __init__(self, pizza):
        super().__init__("Et", pizza, 15.0)


class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__("Sogan", pizza, 3.0)


class Pastirma(Decorator):
    def __init__(self, pizza):
        super().__init__("Pastirma", pizza, 4.0)

class Biftek(Decorator):
    def __init__(self, pizza):
        super().__init__("Biftek", pizza, 10.0)


class Domates(Decorator):
    def __init__(self, pizza):
        super().__init__("Domates", pizza, 15.0)


class Tonbaligi(Decorator):
    def __init__(self, pizza):
        super().__init__("Ton Baligi", pizza, 3.0)


class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__("Misir", pizza, 4.0)

# Created a class that holds the order details.
class OrdersDatabase:
    def __init__(self):
        self.filename = 'Orders_Database.csv'  # CSV file name
        self.fields = ["Name","Surname", "ID", "Credit Card Number", "Credit Card Pass", "CVC", "Description", "Cost", "Order Time"] # column names
        self.file_exists = os.path.exists(self.filename) # File availability

    # Created add_order to add the new orders to the file.
    def add_order(self, name, surname, ID, ccardnum,  ccardpass, ccardcvc, description, cost):
        order_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Order time
        order = [name, surname, ID, ccardnum, ccardpass, ccardcvc, description, cost, order_time]  # New order

        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)

            # Print column names if file does not exist.
            if not self.file_exists:
                writer.writerow(self.fields)
                self.file_exists = True
            
                writer.writerow(order) # Add the order to the file.

# Defining name and surname validation
def stringvalidation(valid):
    valid = str(valid)

    if valid.isdigit():
        return False
    else:
        return True
# Defining card number
def cardalg(ccardnum):
    ccardnum = str(ccardnum)
    
    if not ccardnum.isdigit():
        return False
    elif not len(ccardnum) == 16:
        return False
    elif int(ccardnum[0]) == 0:
        return False
    else:
        return True
        
# Defining card number algorithm
def cardnum(ccardnum):
    x = 0
    for i in range(len(ccardnum)-1, -1, -1):
        digit = int(ccardnum[i])
        if (len(ccardnum) - i) % 2 == 0:
            doubled = digit * 2
            if doubled > 9:
                doubled = doubled - 9
            x += doubled
        else:
            x += digit
    return x % 10 == 0

# Defining CVC-CVI 
def cvcvalidation(cvcvalid):
    cvcvalid = str(cvcvalid)

    if not cvcvalid.isdigit():
        return False
    elif not len(cvcvalid) == 3 and not len(cvcvalid) == 4:
        return False
    else:
        return True

# Defining credit card pass
def cardpassvalidation(cpvalid):
    cpvalid = str(cpvalid)

    if not cpvalid.isdigit():
        return False
    else:
        return True

# Defining TC ID number and algorithm
def validate_tc_id(tc_id):
    
    # Check length of tc_id is 11
    if len(tc_id) != 11:
        return False

    # Check first digit is not zero
    if tc_id[0] == '0':
        return False

    # Check that all characters are digits
    if not tc_id.isdigit():
        return False

    # Calculate the 10th digit of tc_id
    even_sum = sum([int(tc_id[i]) for i in range(0, 9, 2)])
    odd_sum = sum([int(tc_id[i]) for i in range(1, 9, 2)])
    tenth_digit = ((even_sum * 7) - odd_sum) % 10

    # Calculate the 11th digit of tc_id
    total = sum([int(d) for d in tc_id[:-1]])
    eleventh_digit = total % 10

    # Check if calculated digits are equal to actual digits
    if int(tc_id[9]) == tenth_digit and int(tc_id[10]) == eleventh_digit:
        return True
    else:
        return False