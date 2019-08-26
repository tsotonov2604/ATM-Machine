#Tsvety Sotonov
def startup(fname):
    accounts={}
    try:
        fname=open(fname,'r')
        for row in fname:
            row=row.strip('\n')
            users=row.split(',')
            users[3]=float(users[3])
            #print(type(users[3]))
            accounts[users[0]]=users[1:]
        return accounts
            
            #print(users)
        #print(accounts)
    except: 
        print('Cannot get to the file')
        return None


def getUser(accounts):
    #print(accounts)
    try:
        pin = input('Enter a pin: ')
        
        first_name=accounts[pin][0]
        last_name=accounts[pin][1]
        balance=accounts[pin][2]
        #print(pin,first_name,last_name,balance)
        #print(accounts[pin],first_name)
        return accounts[pin],first_name,pin
   
    except:
        print('Incorrect Pin')
        return (None,None)

def menu(first_name):
    print(first_name + ':')
    print('1: Deposit')
    print('2: Withdraw')
    print('3: Check Balance')
    print('4: My Data')
    print('5: Report')
    print('6: Quit')
   
    choices = {1: 'Deposit',2:'Withdraw',3:'Check Balance',4:'My Data',5:'Report',6:'Quit'}

    while True:
        try:
            option = int(input('Enter number: '))
        
            for choice in choices.keys():
                if choice == option:
                    return choice
        except:
            print('Invalid character, try again')
    
        else:
            print('Valid choices are 1,2,3,4,5,6,try again')
            print('1: Deposit')
            print('2: Withdraw')
            print('3: Check Balance')
            print('4: My Data')
            print('5: Report')
            print('6: Quit')
            option = int(input('Enter number: '))
            break
    
def getAmount():
    while True:
        try:
            amount = float(input('Enter an amount to be deposited or withdrawn: '))
            if amount < 0:
                print('Negative amount.Please try again')
            else:
                #print(amount)
                return amount 
        except:
            print('Invalid Amount. Use digits only.')

def deposit(pin,my_dict):
    amount = getAmount()
    my_dict[pin][2] += amount
    return 
    #print(my_dict)

def withdraw(pin, my_dict):
    
    while my_dict[pin][2] != 0:
        amount = getAmount()
        my_dict[pin][2] -= amount
        
        if amount > mydict[pin][2]:
            print('Insufficient funds to complete the transaction')
        return
    
def balance(pin, my_dict):
    return my_dict[pin][2]

def printUserData(pin, my_dict):
    print('First name:',my_dict[pin][0],'Last name:',my_dict[pin][1],'Balance:',my_dict[pin][2])
    return

def printReport(my_dict):
    print('Contents of dictionary:')
    for key,value in my_dict.items():
        print('{:4} {:10} {:10} $ {:10}'.format(key,*value))
    return
    
        
    
        


fname = input('Enter a file name: ')
#startup(fname)

#accounts = startup(fname)
#getUser(accounts)

#first_name = getUser(accounts)[1]
#menu(first_name)

#pin = getUser(accounts)[2]
my_dict=startup(fname)
printReport(my_dict)

#deposit(pin,my_dict)

                  
