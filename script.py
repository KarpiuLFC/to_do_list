list = []
list.append("Learning Python")
list.append("Learning Terraform")

choice = 0
while choice != 5:
    print("======================================================================") 
    print("1. Show available tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Save to file")
    print("5. Exit") 
    print("======================================================================")  
    choice = int(input("Choose your option [1-5]: "))
    index = 0
    
    if choice == 1:
        print()
        print("Its your up to date task list:")
        print()
        file = open("Day.txt" , "r")
        for line in file.readlines():
            list.append(line.strip())
        for task in list:   
            print(str(index) + " " + task) 
            index += 1
        file.close
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
           
    elif choice == 3:
        print()
        remove_task = int(input("Provide a number of task that can be remove from the list: "))
        list.pop(remove_task)
        print()
        print("Its your up to date task list:")
        print()
        for task in list:
            print(str(index) + " " + task)     ##print task
            index += 1
        print()
        
    elif choice == 4:
        file = open("Day.txt","w+")
        for task in list:
            file.write(task + "\n") 
            index += 1
        file.close
                    
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
        
    
    

        
    

    
