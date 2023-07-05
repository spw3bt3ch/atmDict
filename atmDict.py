userAccount = {
    'surname name':'Olujimi',
    'first name':'Samuel',
    'gender':'male',
    'next of kin':'Olujimi Oluwatosin',
    'next of kin mobile number':'09054671469',
    'account number':['2116271273','23423465434'],
    'account type':'savings account',
    'account balance':'200000',
    'bvn':'27773223443',
    'mobile number(s)':['08173970625','09058453376'],
    'email address':'samueloluwapelumi8@gmail.com',
    'userID':'045',
    'userPIN':'1234',
    'contactAddress':{
        'house number':'9',
        'streetName':'Olambe Rd',
        'nearest b/s':'Jimmy bus stop',
        'town':'Olambe',
        'state of residence':'Lagos state',
        'state of Origin':'Oyo state',
    }
}
services = ['1. WITHDRAWAL', '2. TRANSFER', '3. CHECK BVN', '4. CONFIRM ACCUNT NUMBER', '5. CONFIRM YOUR ACCOUNT TYPE']
metaData = userAccount.items()
ad = userAccount.get('contactAddress')
userName1 = userAccount.get('surname name')
userName2 = userAccount.get('first name')
userNames = userName1 + ' ' + userName2
balance = int(userAccount.get('account balance'))
for s in services:
    print(' ')
    print(s)

print(' ')
chooseoption = int(input('.......ENTER A SERVICE.......: '))
print(' ')
print(' ')  
if chooseoption == 1:
    bal = int(userAccount.get('account balance'))
    count = 0
    while (count <= 5):
        userPIN = userAccount.get('userPIN')
        pinC = input('Enter your PIN: ')
        count += 1
        if pinC == userPIN:
            print(f'You are welcome, {userNames}.')
            print(' ')
            amount = int(input('Enter the Amount you want to withdraw: '))
            if amount >= 100 and amount <= bal:
                print(' ')
                print('Please wait while we process your cash...')
                print(' ')
                print('Take your cash')
                print(' ')
                remainingBal = bal - amount
                ClosingBal = userAccount.update({'Closing Account Balance':remainingBal})
                print(f'Your current balance is {remainingBal}.00')
                print(' ')
                if remainingBal < 100:
                    print('Balance is critically low! Please try a lower amount.')
                else:
                    print(f'Thank you, do have a great day {userNames}.')
                print(' ')
            else:
                print(' ')
                print('Insufficient Balance.')
                print('Fund your account and try again later.')
                print(' ')
            break
        else:
            print('Incorrect PIN, please try again.')
            print(' ')
            continue
    while (count > 3):
        print('Too much attempts')
        break

    if count == 1:
        print('You attempted your PIN once out of 5 times')
    else:
        print('....................................................')
        print(f' You attempted your PIN {count}/5 times.')
    print('....................................................')
    print(' ')
else:
    print(' ')
    print('SERVICE NOT AVAILABLE')
    print(' ')
# To count the number of PIN input attempt
print(' ')
print(' ')
print('.....ACCOUNT SUMMARY.....')
print('.........................................................................')
print(f'OPENING ACCOUNT BALANCE: =N= {balance}.00')
print(' ')
print(f'CLOSING ACCOUNT BALANCE: =N={remainingBal}.00')
print(' ')
cb = balance - remainingBal
print(f'TOTAL WITHDRAWAL: =N= {cb}.00')
print('.........................................................................')
print(' ')
print(' ')
print('OTHER DETAILS MEANT FOR ENCRYPTION:...................................................................................................')
print(' ')
for u in userAccount:
    print(userAccount)
    break
print(' ')
print('......................................................................................................................................')
print(' ')
#............................................................................................................
# Still trying to know how many attempts of the user PIN, from which I will be able to set restrictions - 
# This will give birth to ...if the number of attempts is >= 3, something should be executed.
#............................................................................................................