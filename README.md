**WARNING -- For now we are parsing US and CANADA-Addresses only**

# Project Description

**To parse the US and CANADA addresses**

**To map the state code(AZ) to state name(Arizona)**

**To skip the other country addresses**

**Parsing corrections in the city name(multiple word)**

**Some additional keys are added to the output of *usaddress* python module**

**List of States and Cities(multiple word :P ) are included in the code**

# Code
```
from US_address_parser import parse_address
parse_address("455 North 3rd 190 Arizona Center,Phoenix, AZ 85004")
from canada_address_parser import parse_address
parse_address('2620 32nd St. NE Calgary AB T1Y 6B8')
```

# Methods
	- parse_address

# Params
	- text

# Endpoints
## /usparse
## /caparse

# GET API Call
	- http://localhost:9006/usparse?text=455%20North%203rd%20190%20Arizona%20Center,Phoenix,%20AZ%2085040
	- http://localhost:9006/caparse?text=2620%2032nd%20St.%20NE%20Calgary%20AB%20T1Y%206B8

# GUnicorn Command to run
	- nohup /usr/local/bin/gunicorn --name=address_parser --bind=localhost:9006 --log-level=DEBUG --workers=3 --timeout=6000 wsgi:app &
	- use nohup or make a systemctl daemon service
