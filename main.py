#Outputs a menu of options for the User to choose from
#to add data to the budgeting calculator.
def menuOutput():
    print("(1.) Update My Initial Budget")
    print("(2.) Add An Expense")
    print("(3.) Finish and Calculate My Final Budget")
    print()

#Checks that the inputBudget value input by the user is valid,
#and continues to prompt the User until they input a valid value
#(A number greater than 0.)
def validBudget():
    
    #Initializes a validInput variable for the loop to check if the
    #User's input is valid or not.
    validInput = False
    while validInput == False:
        
        #Initializes the variable validString to False.
        validString = False
        
        #Checks if User's input is an integer. 
        #If yes, it is stored it in a temporary variable called inputBudget.
        #If no, the User is prompted again.
        while validString == False:
            try:
                inputBudget = int(input("Total Monthly Budget: "))
                validString = True
            except ValueError:
                print()
                print("Please enter an integer for the total Monthly budget!")
                print()
        
        #If inputBudget value is greater than 0, the validInput variable is
        #set to True (which breaks the loop), and the input value is returned.
        if inputBudget > 0:
            validInput = True
            return inputBudget
        
        #If inputBudget is not greater than 0, the User is informed that they must 
        #input an initial budget that is greater than 0, then the loop starts over.
        else:
            print()
            print("Uh oh... Your initial monthly budget must be greater than $0.")
            print("Let's try that again!")
            print()

#Checks that the inputExpense value input by the user is valid,
#and continues to prompt the User until they input a valid value
#(A number greater than 0.)
def validExpense():
    
    #Initializes a validInput variable for the loop to check if the
    #User's input is valid or not.
    validInput = False
    while validInput == False:
        
        #Initializes the variable validString to False.
        validString = False
       
        #Checks if User's input is an integer. 
        #If yes, it is stored it in a temporary variable called inputExpense.
        #If no, the User is prompted again.
        while validString == False:
            try:
                inputExpense = int(input("Total Monthly Cost: "))
                validString = True
            except ValueError:
                print()
                print("Please enter an integer for the total Monthly Cost!")
                print()
        
        #If inputExpense value is greater than 0, the validInput variable is
        #set to True (which breaks the loop), and the input value is returned.
        if inputExpense > 0:
            validInput = True
            return inputExpense
        
        #If inputExpense is not greater than 0, the User is informed that they must 
        #input an expense that is greater than 0, then the loop starts over.
        else:
            print()
            print("Uh oh... All expenses must be greater than $0.")
            print("Otherwise, it's not really an expense... is it?")
            print("Let's try that again!")
            print()


#Main Program
def main():
    
    #Initializing the variables
    initBudget = 0
    expenses = 0
    finishedAddingData = False
    finBudget = 0
    percBudget = 0

    #Outputs an initial greeting message to the User
    print("Welcome to your new Budgeting Calculator!")
    print("Let's get started!")
    print()
    print("First off, please enter your total monthly budget.")
    
    #Calls the validBudget function and stores the returned value in the
    #initBudget variable.
    initBudget = validBudget()
    
    #Outputs the User's monthly budget and the program continues.
    print()
    print(f"Awesome! It looks like you've got ${initBudget} available to spend each month.")
    print("Let's keep going!")
    print()
    
    #Outputs a message to the User of what to expect next.
    print("Next up, you'll be able to pick from a menu of options to add some data about your finances.")
    print("Feel free to add as much or as little information as you need!")
    print()
    
    #Outputs the menu of options to add data until the User selects the
    #"Finish and Calculate My Final Budget Option", which breaks the loop.
    while finishedAddingData == False:
        
        #Prints the menu of options for the User to choose from.
        print("What would you like to do next?")
        print()
        menuOutput()
        
        #Initializes the menuOption variable, and sets it to the User's input from the prompt.
        menuOption = input("Please Enter 1, 2, or 3: ")
        print()
        
        #If the User entered "1", the validBudget() function is called, and the User is
        #informed that their initial monthly budget has been updated.
        if menuOption == "1":
            print("It looks like you'd like to update your initial budget for the Month!")
            print()
            
            #Updates initBudget variable to the User's new monthly budget,
            #and the menu loops again.
            initBudget = validBudget()
            print()
            print("Great! Thanks for updating your initial budget for me!")
            print(f"It looks like your new monthly budget is ${initBudget}")
            print("Let's keep going!")
            print()
        
        #If the User entered "2", the validExpense function is called.
        elif menuOption == "2":
            print("Alright, let's add a new expense to your list.")
            print("What would you like to label this expense as?")
            print()
            
            #Initializes the validName variable to False.
            validName = False
            
            #Checks that the value input for expName variable is not an empty string.
            while validName == False:
                
                #Prompts User to input a name for the new expense being added.
                expName = input("Expense Name: ")
                
                #If the User input is an empty string, the User is informed that the input
                #must consist of at least one character, and they will prompted to enter a
                #new name.
                if expName == "":
                    print()
                    print("Please enter at least one character to identify this expense.")
                    print()
                
                #validName is set to True, breaking the loop.
                else:
                    validName = True
            print()
            print(f"Great! So, how much do you spend on {expName} each month?")
            
            #Stores the returned value from the validExpense function in the
            #newExpense variable.
            newExpense = validExpense()
            
            #Adds the value of newExpense to the expenses variable (which records total
            #number of expenses).
            expenses += newExpense
            
            #Outputs the monthly cost of the new expense to the User, and the menu loops again.
            print()
            print(f"Got it! Looks like you spend ${newExpense} on {expName} each month.")
            print("Let's keep going!")
            print()
        
        #If the User entered "3", the program double checks if the User is done entering information
        #into the calculator.
        #If they are, the finishedAddingData variable is set to True (breaking the Menu loop),
        #and the program continues.
        #If not, the Menu loops again, and the User can continue adding data.
        elif menuOption == "3":
            
            print("Looks like we're almost done here!")
            print()
            print("This *is* the last step before I calculate your final budget for you though, so...")
            print("I just want to double check real quick:")
            print()
            print("Are you sure you've finished adding all the financial data you need for your final budget?")
            
            #The doubleCheck variable is initialized and set to False.
            doubleCheck = False
            
            #Prompts the User until they input either "Yes" or "No".
            while doubleCheck == False:
                print()
                
                #Stores User's input in variable finalAnswer and
                #changes finalAnswer to lowercase (to avoid case sensitivity errors)
                finalAnswer = input("Please enter Yes or No: ").lower()
                
                #If finalAnswer has value "yes", the doubleCheck and finishedAddingData variables are both
                #set to True, breaking both the inner (Double Check) and outer (Menu) loops, so the program 
                #can continue.
                if finalAnswer == "yes":
                    doubleCheck = True
                    finishedAddingData = True
                
                #If finalAnswer has value "yes", the doubleCheck variable is set to True, breaking
                #the inner loop, and causing the Menu to loop again.
                elif finalAnswer == "no":
                    doubleCheck = True
                    print()
                    print("No worries! Let's keep working!")
                
                #If finalAnswer has any other value besides "yes" or "no", the User is told that 
                #the program didn't understand their input, and are prompted to try again.
                else: 
                    print()
                    print("Sorry, I didn't quite get that...")
           
            
            
        
        #If the User enters anything besides 1, 2, or 3, they are informed that they've
        #input an invalid value and are prompted to try again.
        else:
            print()
            print("Sorry, that's not one of the available options!")
            print("Please only enter the number 1, 2, or 3 as your selection.")
            print("Let's try again!")
            print()
    
    #This part is just me being silly. Hope you get a kick out of it Sophia grader! :)
    print()
    print("AAAAAAAlrighty then!")
    print()
    print("Time for me...")
    print()
    print("To make...")
    print()
    print("SOME MAGIC!!!!")
    print()
    print("After some complex calculations that I won't bore you with...")
    print("I have successfully computed your final monthly budget!")
    print("And I'm proud to tell you...")
    print()
    print("*Drumroll please...*")
    print("....................")
    print("....................")
    print("....................")
    
    #The value of finBudget (the final amount of the User's budget after all expenses are deducted)
    #is set to the value of initBudget minus the value of expenses.
    finBudget = initBudget - expenses
    
    #The value of percBudget (the percentage of the User's budget needed to cover all expenses)
    #is set to the value of expenses divided by the value of initBudget and multiplied by 100,
    #then rounded to 2 decimal places.
    percBudget = round(100* (expenses / initBudget), 2)
    
    #If the value of finBudget is greater than 0, the final budget and percentage are output to the User
    #and they are congratulated for their budgeting skills!
    if finBudget > 0:
        print(f"Your total expenses take up {percBudget}% of your total ${initBudget} monthly budget!")
        print()
        print("So, what does that mean?")
        print("I'll tell you!")
        print()
        print(f"After all ${expenses} worth of your expenses are deducted from your initial budget...")
        print(f"You're left with a whopping final total of ${finBudget}!!!")
        print()
        print("Woohoo!!! You're rich!!! (Just don't spend it all in one place...)")
    
    #If the value of finBudget is exactly 0, the final budget ($0) and percentage (100%) are output to the User
    #and they are congratulated for their unlikely precison budgeting!
    elif finBudget == 0:
        print("Huh.")
        print()
        print("Wow, I'm impressed.")
        print()
        print(f"Your total expenses take up exactly {percBudget}% of your total ${initBudget} monthly budget!")
        print()
        print("So, what does that mean?")
        print("I'll tell you!")
        print()
        print(f"After all ${expenses} worth of your expenses are deducted from your initial budget...")
        print(f"You're left with a whopping final total of... uh... ${finBudget}...")
        print()
        print("I've got to give it to you, that is some PRECISE budgeting!")
        print()
        print("But... Have you ever heard of a Savings Account? Might be worth looking into...")
    
    #If the value of finBudget is less 0, the final budget and percentage are output to the User
    #and they are snarkily advised on how they can bring their spending within reason.
    elif finBudget < 0:
        print("Oh.")
        print()
        print("Um. This is awkward...")
        print()
        print(f"It turns out your total expenses take up {percBudget}% of your total ${initBudget} monthly budget.")
        print()
        print("So, what does that mean?")
        print("Well, it's not *great* news, but somebody has to tell you...")
        print()
        print(f"After all ${expenses} worth of your expenses are deducted from your initial budget...")
        print(f"You're left spending {percBudget - 100}% more than you can afford to spend each month. Yikes.")
        print()
        print("To make it easier for you to understand,")
        print(f"this means you're going to need to spend *at least* ${abs(finBudget)} less each month to stay within your budget.")
        print()
        print("Maybe cool it on the Starbucks? That's what the news says at least... I don't know, I'm just a program...")

#Calls the main function, which runs the bulk of the program for the User.
main()
