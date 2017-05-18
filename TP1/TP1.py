# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "http://api.thesubdb.com/?action=download&hash=edc1981d6459c6111fe36205b4aff6c2&language=pt,en"

# your source coe here


# data to be sent to api

headers = {
    'User-Agent': 'SubDB/1.0 (Pyrrot/0.1; http://github.com/jrhames/pyrrot-cli)',
}

# sending post request and saving response as response object
r = requests.get(url=API_ENDPOINT,headers=headers)



# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)