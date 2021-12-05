'''
Breakfast:Egg Sandwich,Bagel,Coffee
Lunch:BLT,PB&J,Turkey Sandwich
Dinner:Soup,Salad,Spaghetti,Taco
'''

# For List
'''
meuns = [['Egg Sandwich','Bagel','Coffee'],
        ['BLT','PB&J','Turkey Sandwich'],
        ['Soup','Salad','Spaghetti','Taco']]
print("Breakfast:",meuns[0])
print(meuns[0][1])
'''
# For Dictionary
dmeuns = {'Breakfast':['Egg Sandwich','Bagel','Coffee'],
'Lunch':['BLT','PB&J','Turkey Sandwich'],
'Dinner':['Soup','Salad','Spaghetti','Taco']}
'''for i in dmeuns:
    print(i,":",dmeuns.get(i))
'''
for name,meun in dmeuns.items():
    print(name,':',meun)