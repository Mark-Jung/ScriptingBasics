import os
import re
import time
from colorama import Fore, Back, Style
import pandas as pd
from tabulate import tabulate as tb
import numpy as np



#Menu Options
print("[ORDER & PAY HERE]")
NumCust = input("How many of you will be dining with us today?")


#Trying to figure out how to clear out the output to make output cleaner for user
# def ClearOutput():
#     if os.name == 'nt':
#         os.system('cls')
#     else:
#         os.system('clear')
# ClearOutput()

#Item Details: Name & Prices ==> Just edit "ItemDet" to make future amendments
ItemDet = {'Cheese Burger':6, 'Fries':3, 'Tenders': 4, 'Soda':2}
OrderList = list(ItemDet.keys())
ItemP = list(ItemDet.values())

#Make list for KEYS
numOrderList = int(len(OrderList))


# print(Fore.RED+"[MENU]"
#       "\nItem 1 [Cheese Burger]: $6"
#       "\nItem 2 [Fries]: $3"
#       "\nItem 3 [Tenders]: $4"
#       "\nItem 4 [Soda]: $2")

mntbl = {'Item #':list(range(1,numOrderList+1)),
         'Item Name': OrderList,
         'Item Price':ItemP}
mntblDF = pd.DataFrame(mntbl, columns = ['Item #', 'Item Name', 'Item Price'])

print(Fore.RED+"[MENU]")
print(tb(mntblDF,headers='keys',tablefmt='psql'))


#Make list for VALUES through user input
OrderQuant = []
for a in range(1,numOrderList+1):
    print(Fore.BLACK+"How many of Item",a,"would you like to order?")
    quant = int(input("Please indicate the quantity here:"))
    OrderQuant.append(quant)

#Merge two lists above to make dictionary for order_n
merge = {OrderList[i]:OrderQuant[i] for i in range(len(OrderList))}

#Calculating subtotals

#Repeat order back to customer & Record sales in form of receipt
print(Fore.BLUE+"Thank you for dining with us.\nPlease confirm your order.")
OrderData = {'Item #':list(range(1,numOrderList+1)),
             'Item Name': OrderList,
             'Item Price($)': ItemP,
             'Quantity Ordered': OrderQuant
             }

OrderDF = pd.DataFrame(OrderData, columns = ['Item #', 'Item Name', 'Item Price($)','Quantity Ordered'])

OrderDF['Subtotal'] = OrderDF['Item Price($)']*OrderDF['Quantity Ordered']

print(tb(OrderDF,headers='keys',tablefmt='psql'))
print (Fore.BLACK+"Your total payment is:", sum(OrderDF['Subtotal']))


OrderDF.to_excel("Revenue.xlsx",
                 sheet_name='Revenue 2019')


######FOR CUSTOMER######
time.sleep(3)

yes = {'yes','y','ye',''}
no = {'no', 'n'}
sumOrderDF=int(sum(OrderDF['Subtotal']))
splitcheck = sumOrderDF/int(NumCust)

while True:
    done = input(Fore.GREEN + "We hope you enjoyed your meal. Would you like your bill?").lower()
    if done in yes:
        print(Fore.BLACK + "Your total payment is:", sumOrderDF,'dollars.')
        check = input("Would you like to split the check?")
        if check in yes:
            print(Fore.BLACK+"That will be",splitcheck,'dollars each.')
            print("\n Thank you for dining with us. We hope you visit us again!")
            break
        elif check in no:
            print(Fore.BLACK+"The total is",sumOrderDF, "dollars. Please insert the credit card you would like to pay with.")
            print("\nThank you for dining with us. We hope you visit us again!")
            break
    elif done in no:
        print(Fore.BLACK+"We will get back to you later.")
        time.sleep(3)
        continue