order = [0] * 100
n = 0
position = 0
choice = 0
total_price = 0.0

menu = {
    1: {"1]-Jolly Spaghetti with Drink\t\t$5.99": 5.99},
    2: {"[2]-Jolly Spaghetti with 1pc \n    Jolly Crispy chicken & Drink \t$7.99" :7.99},
    3: 14.99,
    4: 7.49,
    5: 8.49,
    6: 9.49,
    7: 10.49,
    8: 13.99,
    9: 26.49,
    10: 32.99,
    11: 45.49,
    12: 2.49,
    13: 2.29,
    14: 1.39,
    15: 4.99,
    16: 4.99,
    17: 4.99,
    18: 1.25,
    19: 3.49,
    20: 2.49,
    21: 3.49,
    22: 2.49,
    23: 3.49,
    24: 2.49,
    25: 3.99,
    26: 1.99,
    27: 7.99,
    28: 5.99,
    29: 8.49,
    30: 6.49,
    31: 6.49,
    32: 7.49,
    33: 6.99,
    34: 8.99
}
print("\n=====================================================")
print("=======================WELCOME=======================")
print("=====================JOLLIBEE INC.===================")
print("=====================================================")
print("\n")
print("\n")
print("\n=====================================================")
print("=========================MENU========================")
print("=====================================================")
print("\n")
print("=====================================================")
print("====================JOLLY SPAGHETTI==================")
print("=====================================================")
print("[1]-Jolly Spaghetti with Drink\t\t$5.99")
print("[2]-Jolly Spaghetti with 1pc \n    Jolly Crispy chicken & Drink \t$7.99")
print("[3]-Jolly Spaghetti Family pack\t\t$14.99")
print("=====================================================")
print("=================JOLLY CRISPY CHICKEN================")
print("=====================================================")
print("[4]-Jolly Crispy Chicken \n    2pc w/ 1 side & Drink \t\t$7.49")
print("[5]-Jolly Crispy Chicken \n    2pc w/ 2 side & Drink \t\t$8.49")
print("[6]-Jolly Crispy Chicken \n    3pc w/ 1 side & Drink \t\t$9.49")
print("[7]-Jolly Crispy Chicken \n    3pc w/ 2 side & Drink \t\t$10.49")
print("[8]-6pc Jolly Crispy \n    Chicken Bucket \t\t\t$13.99")
print("[9]-Bucket treat \n    1 Jolly Crispy Chicken Bucket(6pc) \n    3pcs Mashed Potatos  \n    3pcs Peach Mango Pies \t\t$26.49")
print("[10]-Bucket treat \n    1 Jolly Crispy Chicken Bucket(6pc) \n    1pc Spaghetti family Pack  \n    3pcs Peach Mango Pies \t\t$32.99")
print("[11]-Bucket treat \n    2 Jolly Crispy Chicken Bucket(12pcs) \n    6 Steamed Rice  \n    6 Chocolate Sundaes\t\t\t$45.49")
print("=====================================================")
print("=======================DESSERTS======================")
print("=====================================================")
print("[12]-Peach Mango Pies \t$2.49")
print("[13]-Chcolate Sundae \t$2.29")
print("[14]-Vanilla Twirl \t$1.39")
print("=====================================================")
print("=======================KIDS MEAL=====================")
print("=====================================================")
print("[15]- 1pc Jolly Crispy Chicken \n     w/ Rice & Drink \t\t$4.99")
print("[16]-Jolly Spaghetti w/ Drink \t$4.99")
print("[17]-Yum w/ cheese,\n     Small fries & Drink \t$4.99")
print("=====================================================")
print("=========================SIDES=======================")
print("=====================================================")
print("[18]-Steamed Rice\t$1.25")
print("[19]-Mashed Potato \n     Large\t\t$3.49")
print("[20]-Mashed Potato \n     Regular\t\t$2.49")
print("[21]-Buttered Corn \n     Large\t\t$3.49")
print("[22]-Buttered Corn \n     Regular\t\t$2.49")
print("[23]-French Fries\n     Large\t\t$3.49")
print("[24]-French Fries\n     Regular\t\t$2.49")
print("=====================================================")
print("=======================YUM BURGER====================")
print("=====================================================")
print("[25]-Yum w/ Cheese \n     w/ fries & Drink\t$3.99")
print("[26]-Yum w/ Cheese \n     Regular\t\t$1.99")
print("[27]-Big Yum\n     w/ fries & Drink\t$7.99 ")
print("[28]-Big Yum\n     Regular\t\t$5.99")
print("[29]-Aloha Yum\n     w/ fries & Drink\t$8.49 ")
print("[30]-Aloha Yum\n     Regular\t\t$6.49")
print("=====================================================")
print("=======================BURGER STEAK==================")
print("=====================================================")
print("[31]-2pcs Burger steak w/ Drink \n     1Side\t$6.49")
print("[32]-2pcs Burger steak w/ Drink \n     2Sides\t$7.49 ")
print("=====================================================")
print("======================PALABOK FIESTA=================")
print("=====================================================")
print("[33]-Palabok Fiesta w/ Drink \t$6.99")
print("[34]-Palabok Fiesta w/ 1pc\n     Jolly Crispy Chicken \n     & Drink\t\t\t$8.99")
print("=====================================================")
print("How many Order?")
n = int(input())
print("\n")
print("=====================================================")
print("=================CUSTOMER ORDERS====================")
print("=====================================================")
print("\nWHATS YOUR ORDER?\n")
for i in range(n):
    order[i] = int(input())

for i in range(n):
    if order[i] in menu:
        total_price += menu[order[i]]
print("\n=====================================================")
print("==============CUSTOMER ORDER SUMMARY================")
print("=====================================================")

for i in range(n):
    print(f"Order {i + 1}: {menu[order[i]]}")
print(f"Total Price: ${total_price:.2f}")