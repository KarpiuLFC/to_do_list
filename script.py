choice = 0
while choice != 5:
    print("======================================================================") 
    print("1. Show all your tasks")
    print("2. Add task")
    print("3. Remove task")
    #print("4. Save changes")
    print("4. Export to file")
    print("5. Exit") 
    print("======================================================================")  
    choice = int(input("Choose your option [1-5]: "))
    index = 0
    
    list = []
    list.append("Learning Python")
    list.append("Learning Terraform")
    file = open("Day.txt" , "r") ## "r" - reading
    for line in file.readlines():
        list.append(line.strip()) ## strip - avoid unnecessary characters
    file.close
    
    if choice == 1:
        #list.clear()
        #list.append("Learning Python")
        #list.append("Learning Terraform")
        print()
        print("Its your up to date tasks list:")
        print()
        #file = open("Day.txt" , "r") ## "r" - reading
        #for line in file.readlines():
        #    list.append(line.strip()) ## strip - avoid unnecessary characters
        #file.close
        for task in list:   
            print(str(index) + " " + task) 
            index += 1
        print()
            
    elif choice == 2:
        print()
        new_task = input("Insert new task which will be added to the list: ")
        print()
        print("Its your up to date task list:")
        print()
        list.append(new_task)
        for task in list:   
            print(str(index) + " " + task)     ##print task
            index += 1
        print()
        save=str(input("Do you want to save your changes? (Y/N): "))
        if save == str("Y"):
            #remove_mandatory = ["Learning Python" , "Learning Terraform"] - its always there in the list
                list.pop(0)
                list.pop(0)
                #list.clear()
                file = open("Day.txt","w+") ## "w" - write
                for task in list:
                    file.write(task + "\n") ## "\n" - with new line
                file.close
                print("Changes have been saved")
        elif save == str("N"):
                list.clear()
                file = open("Day.txt","r") ## "w" - write
                for line in file.readlines():
                    list.append(line.strip()) ## strip - avoid unnecessary characters
                file.close
                file = open("Day.txt","w+") ## "w" - write
                for task in list:
                    file.write(task + "\n") ## "\n" - with new line
                file.close
                print ("Changes discarded!")
        else:
                print("Incorrect value has been provided! Please start your job again")
        print()
           
    elif choice == 3:
        print()
        for task in list:   
            print(str(index) + " " + task) 
            index += 1
        print()
        remove_task = int(input("Provide a number of task that can be remove from the list: "))
        if remove_task == 0:
            print()
            print("Important: You cannot remove task 'Learning Python' !!! It's so much important for you")
            print("Select other option or try to remove other task")
            print()
        elif remove_task == 1: 
            print()
            print("Important: You cannot remove task 'Learning Terraform' !!! It's so much important for you")
            print("Select other option or try to remove other task")
            print()
        elif remove_task >= index:
            print()
            print ("Incorrect value has been provided! Please start your job again")
            print()
        else:
            list.pop(remove_task)
            index = 0
            print()
            #print("Its your up to date task list:")
            #print()
            #for task in list:
             #   print(str(index) + " " + task)     ##print task
             #   index += 1
            #print()
            save=str(input("Do you want to save your changes? (Y/N): "))
            if save == str("Y"):
            #remove_mandatory = ["Learning Python" , "Learning Terraform"] - its always there in the list
                list.pop(0)
                list.pop(0)
                #list.clear()
                file = open("Day.txt","w+") ## "w" - write
                for task in list:
                    file.write(task + "\n") ## "\n" - with new line
                file.close
                print("Changes have been saved")
            elif save == str("N"):
                list.clear()
                file = open("Day.txt","r") ## "w" - write
                for line in file.readlines():
                    list.append(line.strip()) ## strip - avoid unnecessary characters
                file.close
                file = open("Day.txt","w+") ## "w" - write
                for task in list:
                    file.write(task + "\n") ## "\n" - with new line
                file.close
                print ("Changes discarded!")
            else:
                print("Incorrect value has been provided! Please start your job again")
            print()
            
    #elif choice == 4:
    #    print()
        #remove_mandatory = ["Learning Python" , "Learning Terraform"] - its always there in the list
    #    list.pop(0)
    #    list.pop(0)
    #    file = open("Day.txt","w+") ## "w" - write
    #    for task in list:
    #        file.write(task + "\n") ## "\n" - with new line
    #    file.close
    #    print("Changes have been saved")
    #    print()
        
    elif choice == 4:
        print()
        file = open("Tasks.txt","w+") ## "w" - write
        for task in list:
            file.write(task + "\n") ## "\n" - with new line
        file.close
        print("Saved to file: Tasks.txt")
        print()
     
        
    elif choice == 5:
        print()
        print("Good job! See you next time")   
        print()     
    else:
        print()
        print("ERROR: Invalid option")
        print()
        print("Select number again in range [1-5]!")
        print()
        
