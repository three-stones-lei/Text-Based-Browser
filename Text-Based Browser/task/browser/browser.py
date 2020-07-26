
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
from collections import deque
import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init
init()
from colorama import Fore, Back, Style

visit_pages = deque()
args = sys.argv
directory = args[1]
if not os.path.exists(directory):
    os.mkdir(directory)
access_addresses = ['bloomberg.com', 'nytimes.com']
tags = ['p', 'a', 'ul', 'ol', 'li']
while True:
    enter_address = input()
    if '.' not in enter_address:
        if enter_address == 'exit':
            break
        elif enter_address == access_addresses[0]:
            with open(f'{directory}/bloomberg.txt', 'r') as f:
                print(f.read())
        elif enter_address == access_addresses[1]:
            with open(f'{directory}/nytimes.txt', 'r') as f:
                print(f.read())
        elif enter_address == 'back':
            if len(visit_pages) > 1:
                visit_pages.pop()
                print(visit_pages.pop())

        else:
            print('Error: Incorrect URL')
            print()
    else:
        if enter_address == access_addresses[0]:
            page_content = []
            with open(f'{directory}/bloomberg.txt', 'w') as f:
                response = requests.get(f'https://{enter_address}')
                soup = BeautifulSoup(response.content, 'html.parser')
                for tag in tags:
                    for p in soup.find_all(tag):
                        print(p.get_text())
                        f.write(p.get_text() + '\n')
                        page_content.append(p.get_text())
            access_addresses[0] = 'bloomberg'
            visit_pages.append('\n'.join(page_content))
        elif enter_address == access_addresses[1]:
            page_content = []
            with open(f'{directory}/nytimes.txt', 'w') as f:
                response = requests.get(f'https://{enter_address}')
                soup = BeautifulSoup(response.content, 'html.parser')
                for tag in tags:
                    for p in soup.find_all(tag):
                        print(p.get_text())
                        f.write(p.get_text() + '\n')
                        page_content.append(p.get_text())
            access_addresses[1] = 'nytimes'
            visit_pages.append('\n'.join(page_content))
        else:
            # print('Error: Incorrect URL')
            page_content = []
            file_name = '_'.join(enter_address.split('.'))
            with open(f'{directory}/{file_name}.txt', 'w') as f:
                response = requests.get(f'https://{enter_address}')
                soup = BeautifulSoup(response.content, 'html.parser')
                soup.prettify()
                for tag in tags:
                    if tag == 'a':
                        for p in soup.find_all(tag):
                            print(Fore.BLUE + p.get_text())
                            f.write(p.get_text() + '\n')
                            page_content.append(p.get_text())
                    else:
                        for p in soup.find_all(tag):
                            print(p.get_text())
                            f.write(p.get_text() + '\n')
                            page_content.append(p.get_text())
            visit_pages.append('\n'.join(page_content))




