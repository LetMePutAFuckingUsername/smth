import requests

link = "https://bank.gov.ua/"
htmlText = requests.get(link)
list1 = htmlText.text.split('<a class="index-link" href="/ua/markets/exchangerates" ')
linkLists = []
for elem in list1:
    linkLists.append(elem[1:elem.find('"')])
print(linkLists)

