from flask import Flask, jsonify
from Database import dbConnection
from Scraper import scraper
import logging

app = Flask(__name__)

# Set up logging for the scraper
logging.basicConfig(filename='./Logs/requests.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Route to trigger the scraper and store data in the database
@app.route('/fetch-data/', methods=['GET'])
def fetch_data_and_store():
    try:
        scraper.scrap()
        # Call your function to get all data from the database
        data = dbConnection.getData()
        # Return the data as a JSON response
        return jsonify(data), 200
    except Exception as e:
        # Return an error JSON response if any error occurs
        return jsonify({"error": str(e)}), 500

# Route to get all data from the database
@app.route('/get-all-data/', methods=['GET'])
def get_all_data():
    try:
        # Call your function to get all data from the database
        data = dbConnection.getData()
        
        # Return the data as a JSON response
        return jsonify(data), 200
    except Exception as e:
        # Return an error JSON response if any error occurs
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
