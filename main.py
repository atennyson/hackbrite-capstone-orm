import db
import model
from tabulate import tabulate


while True:

    query = input("Please choose either select, add, update, or delete. ")

    if "select" in query.lower():
        rows = db.select(model.Games)
        print(tabulate(rows))

        result = input("Would you like to save as a csv file? Y/N: ")

        if result.lower() == "y":
            csv_name = input("What would you like the file name to be? ")
            csv_name += ".csv"

            rows.to_csv(rf'~/Downloads/{csv_name}', index=False)

            print("Your csv file will be in your downloads directory.")
    elif "add" in query.lower():
        row = input("Please enter a game title, developer, started (true/false),"
                    "finished (true/false) separated by spaces ")
        row_list = row.split(" ")

        game = model.Games(title=row_list[0], developer=row_list[1], started=row_list[2].lower == "true",
                           finished=row_list[3].lower == "true")
        db.add(game)
        print("Game added successfully")
    elif "update" in query.lower():
        col = input("What column would you like to update? ")
        title = input("What is the title of the game you are updating? ")
        if "title" in col:
            db.update_title(title, model.Games)
        elif "started" in col:
            stat = input("What is the new status of started for this game? ")
            status = stat.lower() == "true"
            db.update_started(title, model.Games, status)
        elif "finished" in col:
            stat = input("What is the new status of finished for this game? ")
            status = stat.lower() == "true"
            db.update_finished(title, model.Games, status)

        print("Row updated successfully.")
    elif "delete" in query.lower():
        title = input("What is the title of the game you are deleting? ")
        db.delete(model.Games, title)
        print("Row deleted successfully.")

    cont = input("Would you like to run another query? Y/N: ")
    if cont.lower() == "y":
        continue

    print("Thank you for your query, please restart me to make another one!")
    break
