# Codeaza Final Project

## Project Description:

This Project is basically scrapping the data of the stocks upon the request from the remote client if he wants to get all the data in the JSON format.

There are 2 requests that follows in the project:
- fetch-data
- get-all-data

These are the 2 end points of our Flask server. fetch-data will scrap the latest data and provide to the client while get-all-data gives the DB data which is scrapped before.


## Project Requirements:

The Requirement.txt file is attached which described the dependencies. But here are the main tech stack used for this project:

- Flask
- Selenium
- Logging
- Mysql

## Project Startup:

- Make Sure having a setup for the Python 3+
- Clone the Repo
- Run ```pip install -r requirements.txt```.
- Then Run ```python main.py```
- Go to browser Or Postman/Thunderclient to make request to ```http://localhost:5000/```

