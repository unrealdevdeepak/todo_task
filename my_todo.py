import db_helper

def main():
    run = 1
    db_helper.create_table()

    while run:
        print("\n")
        print('1. Insert new task in todo list \n'
              '2. View the todo list \n'
              '3. Delete the task \n'
              '4. Exit \n')
        x = input("Chose any of above option : ")

        if x == "1":
            task = str(input("Enter you todo: "))
            db_helper.data_entry(task)

        elif x == "2":
            db_helper.printData()

        elif x == "3":
            indextodelete = int(input("Enter index to delete : "))
            db_helper.deleteTask(indextodelete)

        elif x == "4":
            run = 0

        else:
            print("Please choose valid option")

    db_helper.closeCursor()

if __name__ == '__main__' : main()