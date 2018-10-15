import usaddress
import re
from typing import Dict, List
import sys 

def canada_test(content: str) -> List[str]:
    return re.findall(r'[A-Z]\d[A-Z][ -]{0,1}[A-Z]\d[A-Z]', content) or re.findall(r'[A-Z]\d[A-Z][ -]{0,1}\d[A-Z]\d', content)

def parse_address(address: str) -> Dict[str, str]:
    address_out = {}
    if address:
        address = ' '.join(address.split(' ')).strip()
        address = re.sub(' +', ' ', address)
        can = canada_test(address)
        if can and ' ' in can[0] and len(can)==1:
            s = re.search(r'[A-Z]\d[A-Z][ ][A-Z]\d[A-Z]', address) or re.search(r'[A-Z]\d[A-Z][ ]\d[A-Z]\d', address)
            if s:
                s = s.span()
                address = address[0:s[0]]+address[s[0]:s[1]].replace(' ','-')+address[s[1]:]
            l = usaddress.parse(address)
            l.append((address, 'Address'))
            l2 = [(t[1],t[0].strip(',')) if type(t[0]) is not list else (t[1],t[0]) for t in l]
            address_out = dict(l2)
    return dict(l2)

if __name__ == '__main__':
    print(parse_address(sys.argv[1]))