#!/usr/bin/python3

<<<<<<< HEAD
"""

requests model

"""



if __name__ == '__main__':
    
    import requests
    
    html = requests.get('https://alx-intranet.hbtn.io/status')
    
    print("Body response:")
    
    print("\t- type: {}".format(html.text.__class__))
    
    print("\t- content: {}".format(html.text))
=======
"""Takes in a URL, sends a request to the URL and"""

import requests





def getStatus():
    
    req = requests.get('https://intranet.hbtn.io/status')
    
    content = req.text
    

    
    print("Body response:")
    
    print("\t- type: {}".format(type(content)))
    
    print("\t- content: {}".format(content))
    

    
if __name__ == "__main__":
    
    getStatus()
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
