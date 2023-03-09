# Database Query Tool

### YOU WILL NEED YOUR OWN POSTGRES DATABASE TO USE THIS TOOL

This is a tool I created that can query my database remotely. It runs completely from the command line, currently doesn't work with any other database out of box. (WIP)

## If you want to alter the code to work with your database:
Store your database info into these variables as we will use these to build the connection string in model.py
You will then have to update the Games object to suit your database's table structure. If you have multiple tables you will need multiple objects.
Make sure to change the object calls in main.py and db.py, again this is a WIP, the future goal is to have this tool work with any database without code alterations.

## Preparing the tool:
You will need to run ```pip install -r requirements.txt``` to make sure you have all the modules needed to run this tool. You will also need to have a venv setup for this tool's directory if you don't want the dependencies in your global environment.

## Running the tool:
To run, make sure you are in the directory where you saved the program and in the command line run ```python3 main.py```
Upon execution of the program it will ask you to enter a which type of SQL query you want to run, if invalid the program will error out and end (WIP). Upon entering "select", as long
as the DB connection and query are valid, the tool will stdout the data you requested to the command line. It then will ask if you would like to save as a csv file.
Either type Y for yes or N for no.

If you choose to save the data, the program will then ask you to name the file. Once named, the file will be saved in your ~/Downloads directory. (MacOS only, windows os still WIP)

Now the program will ask if you would like to make another query, either type Y for yes and N for no. If yes the process will begin again, if no the program
will break out and end the process.

If you choose "add", the program will ask for a game title, develope, if you have started the game, if you have finished the game. If entered correctly, it will store this as a new row in the database.

If you choose "update" it will ask which row you would like to update, title, started, or finished. Choose which row and then give the new value for that row.

If you choose "delete" it will ask which row you like to delete, give the title for that row and if valid the program will remove that row and commit the changes.
