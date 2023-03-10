import pclasses as pclss
import datetime

def main():
    with open("menu.txt", "r") as file:
        for line in file:
            print(line)


def main2():
    with open("menu2.txt", "r") as file:
        for line in file:
            print(line)

# The menu is printed on the screen by calling the function.
main()
taban = int(input("Pizza Tabanı Seçiminiz (1-10): "))
main2()
sos = int(input("Sos Seçiminiz (11-20): "))


# An if-elif-else algorithm has been written to assign pizza and sauce values according to the user's choice.
pizza = None

if taban == 1:
    pizza = pclss.Klasik()
elif taban == 2:
    pizza = pclss.Margarita()
elif taban == 3:
    pizza = pclss.TurkishPizza()
elif taban == 4:
    pizza = pclss.SadePizza()
elif taban == 5:
    pizza = pclss.Newyork()
elif taban == 6:
    pizza = pclss.Italiano()
elif taban == 7:
    pizza = pclss.Callypso()
elif taban == 8:
    pizza = pclss.Konyalim()
elif taban == 9:
    pizza = pclss.Fourcheese()
elif taban == 10:
    pizza = pclss.Ocakbasi()
else:
    print("Geçersiz bir seçim yaptınız. Lütfen kodu tekrar çalıştırıp geçerli bir seçim yapınız.")
    exit()

toppings = None
if sos == 11:
    toppings = pclss.Zeytin(pizza)
elif sos == 12:
    toppings = pclss.Mantar(pizza)
elif sos == 13:
    toppings = pclss.KeciPeyniri(pizza)
elif sos == 14:
    toppings = pclss.Et(pizza)
elif sos == 15:
    toppings = pclss.Sogan(pizza)
elif sos == 16:
    toppings = pclss.Misir(pizza)
elif sos == 17:
    toppings = pclss.Pastirma(pizza)
elif sos == 18:
    toppings = pclss.Biftek(pizza)
elif sos == 19:
    toppings = pclss.Domates(pizza)
elif sos == 20:
    toppings = pclss.Tonbaligi(pizza)
else:
    print("Geçersiz bir seçim yaptınız. Lütfen kodu tekrar çalıştırıp geçerli bir seçim yapınız.")
    exit()

# Order details printed.
print(f"\n{toppings.get_description()} sipariş ettiniz.")
print(f"\nToplam ücret {toppings.get_cost()} TL idir.")


###################
name = input("\nAdınız: ").upper()
while(True):
    if pclss.stringvalidation(name):
        break
    else:
        print("Ad rakam içermez, lütfen geçerli bir isim yazınız!")
        name = input("Adınızı tekrar giriniz: ")

surname = input("\nSoyadınız: ").upper()
while(True):
    if pclss.stringvalidation(surname):
        break
    else:
        print("Soyad rakam içermez, lütfen geçerli bir isim yazınız!")
        surname = input("Soyadınızı tekrar giriniz: ")

ID = input("\nTc Kimlik Numara: ")
while(True):
        if pclss.validate_tc_id(ID): #checking if the credit card number is valid
            break
        else:
            print("Geçersiz Kimlik Numarası!")
            ID = input("Kimlik Numaranızı Tekrar Giriniz: ")

ccardnum = input("\nKredi Kartı Numaranız: ")
while(True):
        if pclss.cardalg(ccardnum) and pclss.cardnum(ccardnum): #checking if the credit card number is valid
            break
        else:
            print("Geçersiz Kredi Kartı Numarası!")
            ccardnum = input("Kredi Kartı Numaranızı Tekrar Giriniz: ")


ccardpass = input("\nKredi Kartı Şifreniz: ")
while(True):
    if pclss.cardpassvalidation(ccardpass):
        break
    else:
        print("Geçersiz Şifre!")
        ccardpass = input("Şifreyi tekrar giriz: ")


ccardcvc = input("CVC Kodunuzu Giriniz: ")
while(True):
    if pclss.cvcvalidation(ccardcvc):
        break
    else:
        print("Geçersiz CVC!")
        ccardcvc = input("CVC'yi tekrar giriz: ")


orderdate = datetime.datetime.now().strftime('%d-%m-%Y')
ordertimehour = datetime.datetime.now().strftime('%H:%M')

print(f"\n{orderdate} Tarihinde Saat {ordertimehour}'de Verdiğiniz {toppings.get_cost()}₺ Tutarındaki {toppings.get_description()} Siparişiniz Hazırlanıyor.")

# An instance of the OrdersDatabase class is created and assigned to the orders_db variable.
orders_db = pclss.OrdersDatabase()
# Used add_order method to add a new order.

orders_db.add_order(name, surname, ID, ccardnum, ccardpass, ccardcvc, toppings.get_description(), toppings.get_cost())