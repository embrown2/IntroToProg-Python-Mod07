#---------------------------------------------------------------------------------#
# Title: Assignment07.py
# Desc: This script demonstrates how Pickling and Structured error handling work.
# Change Log: (Who, When, What)
# EBrown, 8.23.2022, Created File
#----------------------------------------------------------------------------------#

# Import and Define Global Variable
import pickle # Imported code from another file to allow for pickling.
selection = 0 # Defining global variable.

# Define Menu Function
def display_menu():
      print("Please select one of the following:")
      print("(1) Input Data to be Pickled" + "\n" #Data stored in binary in txt file via pickling.
            "(2) Read Pickled Data from File as Python Object" + "\n" #Data loads only one line of txt file.
            "(3) Structured Error Handling Demo" + "\n"
            "(4) Exit")

# Main Script
while selection != "4":
      display_menu()
      selection = input("Please enter a number (1-4):").strip()

      if selection == "1":
            objfile = open("GroceryList.txt","w")
            objfile.write("") # Clears file before each input since pickle.load() can only read one line.
            objfile.close()
            objfile = open("GroceryList.txt", "ab")
            ingredient = str(input("Pick an ingredient:"))
            recipe = str(input("What recipe does it go in?:"))
            new_item = [ingredient, recipe]
            pickle.dump(new_item,objfile)
            objfile.close()
            print("\n" + "***Action 1 complete.***" + "\n")
            continue

      if selection == "2":
            objfile = open("GroceryList.txt","rb")
            objfile_data = pickle.load(objfile)
            print(objfile_data)
            objfile.close()
            print("\n" + "***Action 2 complete.***" + "\n")
            continue

      if selection == "3":
            # Section 1 - No error, code will complete "try" section of script.
            try:
                  var1 = "No"
                  var2 = "errors"
                  var3 = "here!"
                  try_list = [var1, var2, var3]
                  print(*try_list)
            except:
                  print("Error found in first section!")

            # Section 2 - Error, code will default to "except" section of script.
            try:
                  var1 = 100/0
                  print(list)
            except:
                  print("Error found in second section!")
            print("\n" + "***Action 3 complete.***" + "\n")
            continue

if selection == "4":
      print("\n"+"***That's all for now, folks!***"+"\n")
      exit()

# End of script.



