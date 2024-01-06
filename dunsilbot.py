from datetime import datetime
import random, time, requests

def displayMenu(): #Defining the function that displays the menu option
  menu = ['Diary/Notes','Tell me a joke','Random Quotes','What says the time?','Exit']
  print('\n--------MENU----------\n')
  for (i, menu) in enumerate(menu):
    #[(1, Tell me about the team), (2,Tell me ...), ].  [1,2,3,4]
    print(f"{i+1}. {menu}")
  print('\nChoose a number: ')  
    
print("Welcome, I am Dunsil Chatbot.")
time.sleep(0.5) #2 seconds delay/sleep
print("\nI can save your notes (diary),", end="") #end="" to remove newline, time.sleep to display it one after the other.
time.sleep(1)
print(" tell you jokes, give you inspirational quotes, and tell you what says the time.")

time.sleep(1)
name = str(input('\nWhat is your name?  ')) #Request user's name

print(f"\nHello {name}, I'm excited to serve you. How may I help you today?\n") #User greetings



Diary = [] #Defining array to store notes

Joke = ['What kind of exercise do lazy people do? Diddly-squats.',
'What do you call a pony with a cough? A little horse!',
'What is Forrest Gump\'s password? 1Forrest1',
'Why did the M&M go to school? He wanted to be a Smartie.',
'What did one traffic light say to the other? Stop looking at me, I\'m changing!',
'What do you call bears with no ears? B.',
'What\'s a foot long and slippery? A slipper!',
'Why do French people eat snails? They don\'t like fast food',
'What\'s red and moves up and down? A tomato in an elevator!',
'I invented a new word today: Plagiarism.']

## function that gets the random quote
def get_random_quote():
	try:
		## making the get request
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			## extracting the core data
			json_data = response.json()
			data = json_data['data']

			## getting the quote from the data
			print(data[0]['quoteText'])
		else:
			print("Error while getting quote")
	except:
		print("Something went wrong! Try Again!")


Exit = False
returnToMenu = [False, False, False, False]

while Exit is False: #Loop to keep the function displayMenu() running.
  displayMenu()
  try: #Error Handling
    userMenuChoice = int(input(''))
    if userMenuChoice == 1:
      while returnToMenu[0] == False:
        diaryOption = ['Create new note', 'View my notes', 'Return to Main Menu']
        print('')
        for (i, diaryOption) in enumerate(diaryOption):
          print(f"{i+1}. {diaryOption}")
        diaryOptionUserChoice = int(input('\nChoose a number: '))
        if diaryOptionUserChoice == 1:
          Diary.append(str(input('\nPlease insert your notes here: \n')))
        elif diaryOptionUserChoice == 2:
          print('')
          for (i, Diary) in enumerate(Diary):
            print(f"NOTE {i+1}: \n{Diary}\n")
        elif diaryOptionUserChoice == 3:
          returnToMenu[0] = True
          print('\nReturning to main menu')
          time.sleep(1)
          print('***********************')
        input('\nPress ENTER to continue')
    
      
    elif userMenuChoice == 2:
      returnToMenu[1] = False
      while returnToMenu[1] == False:
        try:
          print(random.choice(Joke))
          returnToMenu_1 = int(input('\npress ENTER for more jokes OR \n1. Back to Main Menu'))
          if returnToMenu_1 == 1:
            returnToMenu[1] = True
        except:
          print('')
        
    elif userMenuChoice == 3:
      returnToMenu[2] = False
      while returnToMenu[2] == False:
        try:
          print("Hmm...\n")
          time.sleep(1)
          get_random_quote()
          returnToMenu_2 = int(input('\npress ENTER to continue get another quotes OR \n1. Back to Main Menu: '))
          if returnToMenu_2 == 1:
            returnToMenu[2] = True
            print('\nReturning to main menu')
            time.sleep(1)
            print('***********************')
          input('\nPress ENTER to continue')
        except:
          print('')
  
    elif userMenuChoice == 4:
      Time = datetime.now().strftime(f'%H:%M')
      print("The current time is ", Time) #Added more to the time so there is something to read before the time is displayed
      input('\nPress ENTER to continue')
    elif userMenuChoice == 5:
      Exit = True
      print('Bye, See you soon!')#Added the note for 5, so it does not just end like that.
    elif userMenuChoice > 5:
      print('\nPLEASE ENTER A NUMBER BETWEEN 1 - 5')
      
  except ValueError:
    print("\nPLEASE ENTER A DIGIT!!! ")
    time.sleep(.5)
    print('\nReturning to main menu')
    time.sleep(.5)
    print('***********************')
    time.sleep(.5)
