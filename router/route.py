from router import app
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from datetime import datetime
import re


# DEFAULT
@app.route('/')
@cross_origin()
def default():
          return "Flask Server is running"


# return palindrome and occurances
@app.route('/message', methods=['POST'])
@cross_origin()
def palindromeMessage():

          data = request.get_json()

          # a. Find all palindromes
          palindromes = []
          messages = data['message'].split(" ")
          for message in messages:
                    if len(message) > 2 and message.lower() == message.lower()[::-1]:
                              palindromes.append(message)
          
          queryData = data['query'].replace(' ', '')

          reversed_query = queryData[::-1]
          message = data['message'].replace(' ', '')

          ## b. Count occurrences of the Query string in the Message  
          count_occurance = message.count(queryData)

          ## c. Count occurrences Query string in the Message in reverse
          count_occurance_reverse = message.count(reversed_query) 

          return jsonify({'palindromes': palindromes, 'count_occurance': count_occurance, 'count_occurance_reverse': count_occurance_reverse}), 200