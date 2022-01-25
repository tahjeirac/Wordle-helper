import requests


def constraint(result):
    print(result["word"])
    return True


url = "https://api.datamuse.com/words?sp="
letters = input(
    "what letters do you know, use question marks for unknown spaces: ")
url += letters

contains = input("what letters are contained in it?")
res = requests.get(url)

words = res.json()
if contains:
    filtered_words = print(list(filter(constraint, words)))
    print(filtered_words)
else:
    print(res.json())


# credit to datamuse for use of their api
