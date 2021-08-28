
import pickle
f = open("Database.pkl","wb")
pickle.dump("Fruit Store Database",f)
f.close()
while True:
    ch = int(input("""\n----------Main Menu----------
1. Add Fruit in Store
2. Show Fruit in Store
3. Buy Fruits
4. Calculate Bill
5. Shut Down Application

Enter your choice:"""))
    if ch == 1:
        finfo = {}
        fid = int(input("Enter Fruit ID:"))
        fname = input("Enter Fruit Name:")
        fprice = int(input("Enter Fruit Price(Rs/kg):"))
        finfo = {'ID':fid,'Fruit':fname,'Price(Rs/kg)':fprice}
        print(finfo)
        f = open("Database.pkl","ab")
        pickle.dump(finfo,f)
        f.close()
    elif ch == 2:
        f = open("Database.pkl","rb")
        while True:
            try:
                a=pickle.load(f)
                print(a)
                print(a[ID])
            except EOFError:
                break
        f.close()
    elif ch == 3:
        pass
    elif ch == 4:
        pass
    elif ch == 5:
        print("\nThank You... Visit Again!!!")
        break
    else:
        print("\nInvalid Choice... Try Again!!!")
