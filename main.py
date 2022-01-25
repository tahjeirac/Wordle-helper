import requests
url = "https://api.datamuse.com/words?sp="
letters = input(
    "what letters do you know, use question marks for unknown spaces: ")
url += letters
res = requests.get(url)
print(res.json())

# credit to datamuse for use of their api