#---------------------------------------------------------
# Program Name: Critical Thinking 2 Option 2 - Car Data
# Author: Collin Schaefer
# Date: 30 May 2021
#---------------------------------------------------------
#Pseudocode: This program allows a User to input various
# car data, store data into a dictionary, and print out
# the car data summary from dictionary.
#---------------------------------------------------------
# Program Inputs: Brand, Model, Year, Starting Odometer,
# Ending Odometer, MPG
# Program outputs: 'Brand':Brand, 'Model':Model, 'Year':Year,
# 'Starting Odometer':Starting_Odometer,'Ending_Odometer'
# :Ending_Odometer, 'MPG':MPG 
#---------------------------------------------------------

Brand = input('Enter Car Brand: ')
Model = input('Enter Car Model: ')
Year = int(input('Enter Car Year: '))
Start_Odometer = int(input('Enter Starting Odometer Reading: '))#converts to integer
End_Odometer = int(input('Enter Ending Odometer Reading: ')) #converts to integer
MPG = int(input('Enter Estimated MPG Consumed by Vehicle: ')) #converts to integer

cars = {'Brand':Brand,'Model':Model,'Year':Year,
        'Start_Odometer':Start_Odometer,'End_Odometer':End_Odometer,
        'MPG':MPG}
print(cars)





