import os
from flask import Flask, jsonify, make_response, request, redirect
from US_address_parser import parse_address

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/usparse', methods=['GET', 'POST'])
def address_api():
    if request.method == 'GET':
        text = request.args.get('text')
        address = parse_address(text)
        if address:
            return make_response(jsonify({'Address':address, 'status_code':200}), 200)
        return make_response(jsonify({'error':'sorry! unable to parse', 'status_code':500}), 500)

if __name__ == '__main__':
   app.run(port=9006, debug=False)