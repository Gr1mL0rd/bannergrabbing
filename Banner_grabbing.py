#    this can be used for banner grabbing on recon phase

import socket
import sys
import requests
import json

# grab banner for
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)

# make request we provide
req = requests.get("http://"+sys.argv[1])
print("\n"+str(req.headers))

# fun to get host by name to use this fun we have to import socket
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethostby_+"\n")

# to get IP
# ipinfo.io is an API that provides the IP in log and lat

req_two = requests.get("http://ipinfo.io/"+gethostby_+"/json")
# to use  jason we have to import  json
# we use load function to load the  function with respond
resp_ = json.loads(req_two.text)
print("Location: "+resp_['loc'])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])
