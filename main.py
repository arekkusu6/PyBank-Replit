# still yet to clean all of this up. ex: Be less repetitive in some cases. Functions for headers, etc..
import pyjokes
 
balance = 0;
PIN = int
customers = []

def welcome():
  print('+======================+')
  print('*      Welcome to      *')
  print('*   Universal Banking  *')
  print('+======================+')
  print(' 1) Register')
  print(' 2) Login')
  print(' 3) About')
  print(' 0) Exit')
  print('\nPlease make a selection: ')
  choice = input()
  selection(choice, None)

def selection(choice, name):
  global PIN
  if name == None:
    try:
      choice = int(choice)
      if choice == 1:
        register()
      elif choice == 2:
        login()
      elif choice == 3:
        about()
      elif choice == 0:
        print('Thank you for using the application! :-)')
        exit(0)
      else:
        print('*** Invalid choice. Please try again. ***')
        choice = input()
        selection(choice, None)
    except ValueError:
      print('Please enter a number')
      choice = input()
      selection(choice, None)
  else:
    try:
      choice = int(choice)
      if choice == 1:
        show_balance(name)
      elif choice == 2:
        deposit(name)
      elif choice == 3:
        withdraw(name, PIN)
      elif choice == 0:
        welcome()
      else:
        print('*** Invalid choice. Please try again. ***')
        choice = input()
        selection(choice, None)
    except ValueError:
      print('Please enter a number')
      choice = input()
      selection(choice, None)

def register():
  print('\n Whats your name?: ')
  name = input()
  print('\n+=============================+')
  print(f'\n   Nice to meet you, {name}!  ')
  print(f'\n           WELCOME  ')
  print("\n    to the best damn bank      ")
  print(f'\n  across the entire milky way  ')
  print('\n+=============================+')
  def set_pin():
    global PIN
    print('\n Lets create a PIN: ')
    PIN = input()
    print(f'Your PIN is {PIN}. Is that OK? (y/n)')
    answer = input()
    if answer == "n":
      print('OK, No problem. What would you like your pin to be?: ')
      PIN = input()
      print(f'Your new PIN is {PIN}.')
      account_screen(name, PIN)
    elif answer == "y":
      print(f'Your new PIN is {PIN}.')
      account_screen(name, PIN)
    else:
      print('*** Invalid selection. Please use Y for Yes and N for No ***')
  set_pin()
    
def login():
  global PIN
  print('\n What name is your account under?: ')
  name = input()
  if name.isdigit():
    print('\n *** Invalid. Your Account Name will be a string. ***')
    login()
  else:
    print(f'I got {name}. What was the PIN to that account?: \n (Please do not share your PIN with anyone but us)')
    PIN = input()
    print(f'I got the Account under {name}, with the PIN {PIN}. \n Is that right? (y/n): ')
    ans = input()
    if ans == "n":
      print('OK, No problem. Lets try that again')
      login()
    elif ans == "y":
      account_screen(name, PIN)
    else:
      print('*** Invalid selection. Please use Y for Yes and N for No ***')

def about():
    print('\n A little curious about the app? Great. What would you like to know?')
    print('\n 1) Program')
    print(' 2) Developer')
    print(' 3) Random Joke Generator? Why not.')
    print(' 0) Go Back')
    answ = int(input())
    if (answ == 1):
      print('Woah! Little curious? Cool. Well, I mean this is definitley *not* a console based banking application written in python3. If anything, the main attraction is the Random Joke Generator in the about section ;)')
      print('\n Enter Any Key to Continue:')
      if input():
        welcome()      
    elif (answ == 2):
      print('\n Well, well.. how the tables have turned. Someone cares! My name is Alex btw. I developed this after doing a tutorial of the same type of App but in Java. I figured I knew python3 enough to do it on my own. Might use tkinter in my IDE to get a GUI up and running! github: @beyoutoday')
      print('\n Tech is where its at. It will forever be a passion of mine. Coding does not feel like work at all :) Gradute from a Coding Bootcamp, and a full time dad')
      print('\n Enter Any Key to Continue:')
      if input():
        welcome()   
    elif (answ == 3):
      joke_generator()
    elif (answ == 0):
      welcome()  
    else:
      print('*** Invalid. Please try again. ***')
      
def joke_generator():
  print('\n Ready for some jokes? Enter Y to generate a joke, N to quit.')
  joke_choice = input()
  if (joke_choice == 'y'):
    joke1 = pyjokes.get_joke(language='en', category= 'all')  
    print(f'\n {joke1}')
    joke_generator()
  elif (joke_choice == 'n'):
    about()
  else:
    print('*** Invalid. Please try again. ***')
    joke_generator()
  
def account_screen(name, PIN):
  print('+==============================+')
  print(f'          Welcome back         ')
  print('+==============================+')
  print('\n 1) Balance')
  print('\n 2) Deposit')
  print('\n 3) Withdraw')
  print('\n 0) Logout')
  print(f'\n Whats next, {name}?: ')
  choice = int(input())
  selection(choice, name)

def show_balance(name):
  global balance
  balance = balance
  print(f'This is your balance (${balance}).')
  print('Enter Any Key to Continue:')
  if input():
    account_screen(name, None)
  
def deposit(name):
  print('How much were you looking to deposit?: ')
  try:
    depo = int(input())
    global balance 
    balance = depo + balance
    print(f'\n You deposited a total of ${depo}. Your new balance is now ${balance}')
    print('\n Enter Any Key to Continue:')
    if input():
      account_screen(name, None)
  except ValueError:
    print('*** Your deposit must be a number. ***')

def withdraw(name, PIN):
  global balance
  print('Please Enter your PIN: ')
  PIN_entry = input()
  if (PIN_entry != PIN):
    print('*** Wrong PIN. Try again ***')
    withdraw(name, PIN)
  else:
    print('How much would you like to withdraw?:')
    withdrawn = int(input())
    balance = balance - withdrawn
    print(f'You have withdrawn ${withdrawn}. Your new balance is ${balance}')
    print('Enter Any Key to Contine')
    if input():
      account_screen(name, PIN)  


welcome()