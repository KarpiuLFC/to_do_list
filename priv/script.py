def saving(save): #define function
        #save=str(input("Do you want to save your changes? (Y/N): ")) # after task is added to the list we ask user if newly updated list will be saved
    if save == str("Y"): # if user select Y 
                list.pop(0) # remove_mandatory = ["Learning Python"] its always as a top on the list from the file, but there is still on the list in script engine
                list.pop(0) # remove_mandatory = ["Learning Terraform"] - its top on the list when "Learning Python" has been removed from the list, but there is still on the list in script engine
                file = open("Day.txt","w+") # open file with "w" - write
                for task in list: # for each task 
                    file.write(task + "\n") # write each task (except mandatories - Python and Terraform) in the file: "\n" - with new line
                file.close # close file
                print("Changes have been saved")
    elif save == str("N"): # if user doesnt want to save
                list.clear() # remove all entries on the list, nothing on the list except mandatories - Python and Terraform
                file = open("Day.txt","r") # open file "w" - write
                for line in file.readlines(): # read all lines in file and add value of the line to the list
                    list.append(line.strip()) # add value of each line to list of tasks: strip - avoid unnecessary characters, so we have again both mandatories and task kept in the file
                file.close # close file 
                file = open("Day.txt","w+") # but open it again "w" - write
                for task in list: # all previous tasks are saved in the file which is loaded at the begining of the script (while user selects 1)
                    file.write(task + "\n") # save tasks in the file  "\n" - with new line
                file.close # close file
                print ("Changes discarded!")
    else:
                print("Incorrect value has been provided! Please start your job again")
    print()

choice = 0 # initial value of selection
while choice != 5: # till selection is not equal 5 continue a below loop - if you select 5 then script stop
    print("======================================================================") 
    print("1. Show all your tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Export to file")
    print("5. Exit") 
    print("======================================================================")  
    choice = input("Choose your option [1-5]: ") # Asking user to select above options
    index = 0 # start lising tasks with 0

    list = [] # definition list of tasks
    list.append("Learning Python") # always start with "Learning Python" and always exists
    list.append("Learning Terraform") # always exists task "Learning Terraform"
    file = open("Day.txt" , "r+") ## open file and reading, "a+" if file is not existing then create a new one
    for line in file.readlines(): # read all lines in file and add value of the line to the list
        list.append(line.strip()) # add value of each line to list of tasks: strip - avoid unnecessary characters
    file.close # close file    
    
    try:
        int(choice)/1 # check if provided value is able to be divided by 1 - to avoid incorrect values like 1.5, strings or invalid characters
    except ValueError: # if value error like strings or invalid characters appear then display a below message
        print ()
        print ("Invalid characters. Please provide a digit [1-5]")
        print ()
        continue # but continue further with scripts
        
    if int(choice) == 1: # if user selects 1
        print()
        print("Its your up to date tasks list:")
        print()
        for task in list:   # for each task on the list
            print(str(index) + " " + task) # print value of index starting with 0 and increasing by 1 and print tasks from the list with new line
            index += 1 # increase value by 1
        print()
            
    elif int(choice) == 2: # if user selects 2
        print()
        new_task = input("Insert new task which will be added to the list: ") # ask for new task to be added to list
        print()
        print("Its your up to date task list:")
        print()
        list.append(new_task) # extend list with new added task
        for task in list:   
            print(str(index) + " " + task)     # print value of index starting with 0 and increasing by 1 and print tasks from the list with new line
            index += 1 # increase value by 1
        print()
        save=str(input("Do you want to save your changes? (Y/N): ")) # after task is added to the list we ask user if newly updated list will be saved
        saving(save) #call funtion saving
        
    elif int(choice) == 3: # is user selects 3
        print()
        for task in list:  # for each task on the list
            print(str(index) + " " + task) # print all tasks with new line
            index += 1 # increase value by 1
        print()
        remove_task = int(input("Provide a number of task that can be remove from the list: ")) # user selects which task will be removed from the list by pointing on index value
        if remove_task == 0: # cannot remove task "Learning Python" its mandatory 
            print()
            print("Important: You cannot remove task 'Learning Python' !!! It's so much important for you")
            print("Select other option or try to remove other task")
            print()
        elif remove_task == 1: # cannot remove task "Learning Terraform" its mandatory
            print()
            print("Important: You cannot remove task 'Learning Terraform' !!! It's so much important for you")
            print("Select other option or try to remove other task")
            print()
        elif remove_task >= index: # if user selects task with not existing value of task index
            print()
            print ("Incorrect value has been provided! Please start your job again")
            print()
        else:
            list.pop(remove_task) # if selection is possible then remove it from the list
            index = 0
            print()
            save=str(input("Do you want to save your changes? (Y/N): ")) # ask user if he wants to save a changes
            saving(save) # call function saving
                   
    elif int(choice) == 4:
        name = str(input("Please provide name of file: ")) # ask user how file will be called
        file = open(name + ".txt","w+") # taking a file_name from user "w" - write
        for task in list: # all tasks from the list of script engine
            file.write(task + "\n") # and save them in the list with name provided by user "\n" - with new line
        file.close # file close
        print("Saved to file: " + name + ".txt")
        print()
      
    elif int(choice) == 5: # if user selects 5 then print below message and script stops based on while loop definition 
        print()
        print("Good job! See you next time")   
        print()  
        break
    
    else: # if user selection is out of range selection [1-5] but script will be continue
        print()
        print("ERROR: Invalid character")
        print()
        print("Select number again in range [1-5]!")
        print()
