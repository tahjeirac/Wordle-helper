import requests


url = "https://api.datamuse.com/words?sp="
letters = input(
    "what letters do you know, use question marks for unknown spaces: ")
url += letters

contains = input("what letters are contained in it?")
res = requests.get(url)


def constraint(result):
    word = result["word"]
    for letter in contains:
        if letter not in word:
            return False

    return True


words = res.json()
if contains:
    print(list(filter(constraint, words)))
else:
    print(res.json())


# credit to datamuse for use of their api
