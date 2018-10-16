import os
from flask import Flask, jsonify, make_response, request, redirect
import US_address_parser
import canada_address_parser

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/usparse', methods=['GET', 'POST'])
def us_api():
    if request.method == 'GET':
        text = request.args.get('text')
        address = US_address_parser.parse_address(text)
        if address:
            return make_response(jsonify({'Address':address, 'status_code':200}), 200)
        return make_response(jsonify({'error':'sorry! unable to parse', 'status_code':500}), 500)

@app.route('/caparse', methods=['GET', 'POST'])
def ca_api():
    if request.method == 'GET':
        text = request.args.get('text')
        address = canada_address_parser.parse_address(text)
        if address:
            return make_response(jsonify({'Address':address, 'status_code':200}), 200)
        return make_response(jsonify({'error':'sorry! unable to parse', 'status_code':500}), 500)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=9006, debug=False)