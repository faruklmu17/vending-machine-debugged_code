# displaying product information here
print("Product Code for Coke - 1001\nProduct Code for Kitkat - 1002")
print("Type a product code to continue...")

productCode = int(input())


# coke price is saved as $2.50
cokePrice = 2.50

#checking if the customer has typed 1001

if productCode == 1001:

    # showing the details of the Coke here

    print("You have selected Coke. Please Pay $"+str(cokePrice))

    # allowing the customer to insert money here
    insertedMoney = float(input())

    # checking if the money entered is equal to the cokePrice
    if insertedMoney == cokePrice:
        print("Dispensing Coke...")

    # checking if the money entered is less than the cokePrice

    elif insertedMoney < cokePrice:
      requiredMoney = cokePrice-insertedMoney
      print("Not enough. Please insert $",requiredMoney,"to get the Coke")

    # checking if the money entered is more than the cokePrice
    elif insertedMoney > cokePrice:
        changeMoney = insertedMoney-cokePrice
        print("Your change $",changeMoney,"will be dispensed along with the Coke!")


#checking if the customer has typed 1002
elif productCode == 1002:
    # showing the details of the Kitkat here
    print("You have selected Kitkat. Please Pay $1.75")

    #kitkat price is saved in a variable 
    kitkatPrice = 1.75

    # allowing the customer to insert money here
    insertedMoney = float(input())

    # checking if the money entered is equal to the kitkatPrice

    if insertedMoney == kitkatPrice:
        print("Dispensing kitkat...")

    # checking if the money entered is more than the kitkatPrice 

    elif insertedMoney > kitkatPrice:
        changeMoney = insertedMoney-kitkatPrice
        print("Your change $",changeMoney,"will be dispensed along with the Kitkat!")

    # checking if the money entered is less than the kitkatPrice

    elif insertedMoney < kitkatPrice:
      requiredMoney = kitkatPrice-insertedMoney
      print("Not enough. Please insert $",requiredMoney,"to get the Kitkat")

#what if the customer does not type any valid product code?

else:
    print("Sorry, the code is invalid! Try again.")
