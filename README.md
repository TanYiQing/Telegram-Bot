## Requirements for Assignment-2
[Read the instruction](https://github.com/STIW3054-A211/e-sulam/blob/main/Assignment-2.md)

## Your Info:
1. Matric Number & Name & Photo & Phone Number

|             Name             | Matric No |  Phone Number   |                    Image                   |
| :--------------------------: | :-------: | :-------------: |  :---------------------------------------: |
|         Tan Yi Qing          |  270607   |  +60103373137   |   ![tan's photo](./images/tanyiqing.png)   |
2. Other related info (if any)

## Introduction
<p align="justify">This assignment is the extension from previous assignment 1. This assignment will focus on deploy telegram-bot that can retrieve data from database, and reply the information to user. In this telegram bot, there will have a menu that is constructed with inline keyboard. Besides that, user can also input their IC Number and Phone Number to request more information from the database.</p>

## Deployment Guide
1. Transform this project from sqlite (Assignment 1) to Postgres (Assignment 2).
   
    1.1. Get the credentials from postgresql setting in Heroku (Host, Database, User, Port, Password, URI, Heroku CLI).
    1.2.  In settings.py, change the default database's setting with the credentials get just now.
    1.3.  Configure the database with imported postgresql.
         ![1.3 photo](./images/1.3.png)
2. Create a folder (telegram-bot in my case) and put the python code for telegram bot inside.
3. Deploy the code to Heroku.

    3.1. In the folder created to store the python code for telegram bot, create a `__init__.py`.

    3.2. In Procfile, configure the worker to work the telegram-bot. 
    
    3.3. Reset dynos with `heroku ps:scale worker=1`

    3.4. Deploy to heroku.


## Result/Output (Screenshot of the output)
## Youtube Presentation
## List of Python packages (including the version) used for this system
## References (Not less than 10)
