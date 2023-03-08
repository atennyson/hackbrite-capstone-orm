import db
import model
from tabulate import tabulate

# Endless loop for user to run as many queries as they want, breaks when they say no to running another query.
while True:
    # Asks the user what type of query they want to run.
    query = input("Please choose either select, add, update, or delete. ")

    # Logic for the select query, calls the select function from the db module and prints the returned data.
    if "select" in query.lower():
        rows = db.select(model.Games)
        print(tabulate(rows))

        # User can store the data as a csv file on their local machine if they like
        result = input("Would you like to save as a csv file? Y/N: ")

        # If they choose to do so, they can name the file and the program will automatically attach .csv to the end.
        if result.lower() == "y":
            csv_name = input("What would you like the file name to be? ")
            csv_name += ".csv"

            # For simplicity, the program will save the file to their Downloads directory
            rows.to_csv(rf'~/Downloads/{csv_name}', index=False)

            print("Your csv file will be in your downloads directory.")

    # Logic for the insert query, calls the add function from db and stores the new data in the database.
    elif "add" in query.lower():
        # Asks the user to enter a title, developer, if they have started, and if they have finished to
        # store in the database
        title = input("Please enter a game title: ")
        developer = input("Please enter the developer: ")
        started = input("Please enter if you have started the game (true/false): ")
        finished = input("Please enter if you have finished the game (true/false): ")

        # Creates an instance of a Game object
        game = model.Games(title=title, developer=developer, started=started.lower == "true",
                           finished=finished.lower == "true")

        # Sends the instance of the Game object to the add function in db.
        db.add(game)
        print("Game added successfully")

    # Logic for the update query, calls the update function from db and stores the updated data in the database.
    elif "update" in query.lower():

        # Asks the user to enter the column and title of the game they want to update.
        col = input("What column would you like to update? ")
        title = input("What is the title of the game you are updating? ")

        # If they want to update the title column, they have to enter a new title and that gets sent to the update_title
        # function in db along with the title that is being updated and the Game object.
        if "title" in col:
            new_title = input("What is the new title of the game? ")
            db.update_title(new_title, title, model.Games)

        # If they want to update the started column, they have to enter a new status (True or False) and that gets sent
        # to the update_started function in db along with the title that is being updated and the Game object.
        elif "started" in col:
            stat = input("What is the new status of started for this game? ")
            status = stat.lower() == "true"
            db.update_started(title, model.Games, status)

        # If they want to update the finished column, they have to enter a new status (True or False) and that gets sent
        # to the update_finished function in db along with the title that is being updated and the Game object.
        elif "finished" in col:
            stat = input("What is the new status of finished for this game? ")
            status = stat.lower() == "true"
            db.update_finished(title, model.Games, status)

        print("Row updated successfully.")

    # Logic for the delete query, calls the delete function from db and deletes the row from the database.
    elif "delete" in query.lower():

        # User is asked to give the title of the game for the row they want to delete. This gets sent to the delete
        # function and lets the user know it was successful.
        title = input("What is the title of the game you are deleting? ")
        db.delete(model.Games, title)
        print("Row deleted successfully.")

    # Prompts the user to submit if they would like to run another query or exit the program (y or n)
    cont = input("Would you like to run another query? Y/N: ")

    # If they select yes, then the loop will start over
    if cont.lower() == "y":
        continue

    # If they select no, the program will break from the loop and thank them for using it.
    print("Thank you for your query, please restart me to make another one!")
    break
