'''
Real world Example: Multithreading for I/O bound Tasks
scenario web scrapping
Web scrapping often involves making numerous network request to
fetch web pages.These tasks are I/O bound because they spend a lot
of time waiting for response from servers.Multithreading can significantly
improve the performance by allowing multiple web pages to be fetch concurently

'''

urls=[""]
#advantage of multi threading is we feed it with 3 threads 
#and then we ask it to pull the data from all the 3 urls

import threading
import requests
from bs4 import BeautifulSoup

url=[""]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'fetched{len(soup.txt)}, characters from{url}')

threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All web pages fetched')

