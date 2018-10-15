**WARNING -- For now we are parsing US-Addresses only**

# Project Description

**To parse the US addresses**

**To map the state code(AZ) to state name(Arizona)**

**To skip the other country addresses**

**Parsing corrections in the city name(multiple word)**

**Some additional keys are added to the output of *usaddress* python module**

**List of States and Cities(multiple word :P ) are included in the code**

# Code
```
from US_address_parser import parse_address
parse_address("455 North 3rd 190 Arizona Center,Phoenix, AZ 85004")
```

# Methods
	- parse_address

# Params
	- text

# GET API Call
	- http://localhost:9006/usparse?text=455%20North%203rd%20190%20Arizona%20Center,Phoenix,%20AZ%2085040

# GUnicorn Command to run
	- nohup /usr/local/bin/gunicorn --name=address_parser --bind=localhost:9006 --log-level=DEBUG --workers=3 --timeout=6000 wsgi:app &
