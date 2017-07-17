#CarWorld-A Car Renting System In Python
carinhand = ['Duster', 'Audi', 'jaguar','auto']
totalcar = ['Ford', 'Duster', 'Celerio', 'Audi', 'Jaguar']
carinrent = ['Ford', 'Celerio']
Ford = {
    'Reg No.': 'KL 05 6567',
    'Colour': 'SILVER',
    'Available': 'No',
    'Rent date': '1/06/2016',
    'Return Date': '14/06/2016',
    'Rented to': 'name',
    'price': '$67',
    }
Duster = {
    'Reg No.': 'KL 05 A 768',
    'Colour': 'White',
    'Available': 'Yes',
    'Rent date': '1/06/2016',
    'Return Date': '14/06/2016',
    'Rented to': 'NIL',
    'price': '$40',
    }
Celerio = {
    'Reg No.': 'KL 05 A 3090',
    'Colour': 'Green',
    'Available': 'No',
    'Rent date': '1/06/2016',
    'Return Date': '14/06/2016',
    'Rented to': 'name',
    'price': '$30',
    }
Audi = {
    'Reg No.': 'KL 05 E 8039',
    'Colour': 'Blue',
    'Available': 'Yes',
    'Rent date': '1/06/2016',
    'Return Date': '14/06/2016',
    'Rented to': 'NIL',
    'price': '$70',
    }
Jaguar = {
    'Reg No.': 'KL 05 B 2345',
    'Colour': 'White',
    'Available': 'Yes',
    'Rent date': '1/06/2016',
    'Return Date': '14/06/2016',
    'Rented to': 'NIL',
    'price': '$50',
    }


def carlist():
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        print ('''\n1.Complete list of cars \n2.Available Cars \n3.Cars in lease \n4.back to main menu''')
        choice = input('enter your choice')
        if choice == 1:
            for i in totalcar:
                print (i)
        elif choice == 2:
            for k in carinhand:
                print (k)
        elif choice == 3:
            for l in carinrent:
                print (l)
            
    ch = raw_input('Do you want to check another list ??Y|N:')


def cardetails():
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        for i in totalcar:
            print (i)
        choice = input('Enter name of car')
        for (k, v) in choice.items():
            print (k, ':', v)
        ch = raw_input('Do you want to check another Car ??Y|N:\n')


def rentcar():
    b = 'a'
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        for i in carinhand:
            print i
        choice1 = raw_input('Enter name of car')
        choice = eval(choice1)
        print choice1
        for (k, v) in choice.items():
            print (k, ':', v)
        needcar = raw_input('do you need this car?? Y|N:\n')
        if needcar == 'Y' or needcar == 'y':
            #print choice
            #print 'choice'
            carinhand.remove(choice1)
            carinrent.append(choice1)
            choice['Available'] = 'No'
            choice['Rented to'] = raw_input('enter customer name')
            choice['Rent date'] = raw_input('from date')
            choice['Return Date'] = raw_input('return date')
        ch = raw_input('Do you want to check another Car ??Y|N:\n')   

def submitcar():
    b = 'a'
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        for i in carinrent:
            print i
        choice1 = raw_input('Enter name of car')
        choice = eval(choice1)
        print choice1
        for (k, v) in choice.items():
            print (k, ':', v)
        subcar = raw_input('are you returning this car?? Y|N:\n')
        if subcar == 'Y' or subcar == 'y':
            carinrent.remove(choice1)
            carinhand.append(choice1)
            choice['Available'] = 'Yes'
            choice['Rented to'] = "Nil"
            choice['Rent date'] = "nil"
            choice['Return Date'] = "Nil"

        ch = raw_input('Do you want to check another Car ??Y|N:\n')

print"\t\t CAR RENTING SYSTEM IN PYTHON\t\t\t\t\t"
print"\t\t------------------------------------\t\t\t\t\t\t"
ch='y'
while (ch=='y' or ch=='Y'):
    print "1.List of car \n2.Rent a car\n3.Details of car\n4.number of cars\n5.Return a car "
    choice=input("Enter your choice:")
    if choice==1:
        carlist()
    elif choice==2:
        rentcar()
    elif choice==3:
        cardetails()
    elif choice==4:
        print"1.number of available cars\n2.number of rented cars \n3.totatal number of cars"
        check=input("enter tour choice")
        if check==1:
            print "number of available cars :",len(carinhand)
        elif check==2:
            print "number of rented cars :" , len (carinrent)
        elif check==3:
            print "total number of car:" ,len(totalcar)
    elif choice==5:
        submitcar()
    else:
            exit()
ch=raw_input("do you want to continueY|N:")
