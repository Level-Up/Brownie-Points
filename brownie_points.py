import settings
import requests
import json

# Authenticate
payload = {"userID": settings.USER, "secretKey": settings.PASS}
auth_response = requests.post("https://juliet-api.herokuapp.com/authenticate", data=payload)
auth_data = json.loads(auth_response.text)

if "error" not in auth_data:
    # We should have an auth key now
    if "authenticationToken" in auth_data:
        # Lets show your other half how much you looooooove them
        payload = {"authenticationToken": auth_data["authenticationToken"]}
        nudge_response = requests.post("https://juliet-api.herokuapp.com/send/nudge", data=payload)
        nudge_data = json.loads(nudge_response.text)
        
        if "error" in nudge_data:
            print "Whoops. Somethings gone wrong. I give up."
            print nudge_response.text
        else:
            print "Gosh! You're so thoughtful!"
    else:
        print "Something screwed up. Have a look"
        print auth_response.text
else:
    print "You typo'd your login details. Check settings.py"
