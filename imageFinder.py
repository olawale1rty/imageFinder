import os, sys, requests
from bs4 import BeautifulSoup

def search_result(item):
	search_url = "https://www.google.com/search?q=" + str(item) + "&sxsrf=ALeKk01ODVHD0zXpsToprg5fyTqer5PlyA:1596375844588&source=lnms&tbm=isch&sa=X&ved=2ahUKEwja35O50_zqAhUBnVwKHWHpBm4Q_AUoAXoECBIQAw&biw=1024&bih=465"
	response = requests.get(search_url)
	response_html = BeautifulSoup(response.text, "html.parser")

	result = []
	for i in response_html.findAll("div", {"class": "RAyV4b"}):
		result.append(
            i.find("img")["src"]
        )
	return result[0]

if __name__ == "__main__":
    print("\nWelcome to Image Finder.")

    if len(sys.argv) == 2 :
        item = sys.argv[1]
    else:
        item = input("\nEnter a word to search for... ")
    search_result = search_result(item)
    print("\nThis is the link to your picture -:", search_result)
    print("\nThank you for using my image finder.")