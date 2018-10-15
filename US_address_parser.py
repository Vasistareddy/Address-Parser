import usaddress
import re
from typing import Dict
import ast, sys

states = {'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'MT': 'Montana', 'NA': 'National', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming'}
cities = ast.literal_eval(open('cities.txt').readlines()[0])

def parse_address(address: str) -> Dict[str, str]: 
    address_out = {}
    if address:
        address = ' '.join(address.split(' '))
        address = re.sub(' +', ' ', address).strip()
        pincodes = re.findall(r'\b[A-Za-z]{2}[ ]{0,1}\d{5}\b', address)
        if pincodes:
            l = usaddress.parse(address)
            l.append((address, 'Address'))
            l2 = [(t[1],t[0].strip(',')) if type(t[0]) is not list else (t[1],t[0]) for t in l]
            address_out = dict(l2)
            try:
                if address_out['StateName'] and len(address_out['StateName']) == 2:
                    address_out['StateCode'] = address_out['StateName'].upper()
                    address_out['StateName'] = states[address_out['StateName'].upper()]
            except KeyError:
                address_out = {}

        matches = [city for city in cities if address_out['PlaceName'] in city]
        if len(matches) == 1:
            address_out['PlaceName'] = matches[0]
        elif len(matches) > 1:
            matches = re.findall(r'\w+[.][ ]{}'.format(address_out['PlaceName']), address, re.IGNORECASE)
            address_out['PlaceName'] = matches[0] if matches else address_out['PlaceName']
    return address_out

if __name__ == '__main__':
    print(parse_address(sys.argv[1]))
