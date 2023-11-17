import sqlite3

def RestaurantData():
    Connect=sqlite3.connect("Restaurant.db")
    cur=Connect.cursor()
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS Restaurant(
       Reference TEXT PRIMARY KEY,
       Manchow_Soup TEXT,
       Noodle TEXT,
       Tandoor_Chicken TEXT,
       Chicken_Biryani TEXT,
       Mutton_Biryani TEXT,
       Drinks TEXT,
       Cost_Of_Meals TEXT,
       Service_Charge TEXT,
       State_Tax TEXT,
       Subtotal TEXT,
       Total_Cost TEXT
    );
    ''')
    Connect.commit()
    Connect.close()

def AddRestaurantRecord(Reference,ManchoSoup,Noodle,TandoorChicken,ChickenBiryani,MuttonBiryani,Drinks,CostOfMeals,ServiceCharge,StateTax,Subtotal,TotalCost):
    Connect=sqlite3.connect("Restaurant.db")
    cur=Connect.cursor()
    cur.execute('''INSERT INTO Restaurant VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ) ''', ( Reference, ManchoSoup, Noodle, TandoorChicken, ChickenBiryani, MuttonBiryani, Drinks, CostOfMeals, ServiceCharge,StateTax, Subtotal, TotalCost ))
    Connect.commit()
    Connect.close()


RestaurantData()
