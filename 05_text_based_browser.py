

# run file from command line with a directory name as first and only cmd-argument.
# the directory will be created and used as a place to save websites to.


import os
import sys
import requests
from bs4 import BeautifulSoup

from colorama import init, Fore
init()


# using command line argument to create a dir
dir_name = sys.argv[1]
try:
    os.mkdir(dir_name)
except FileExistsError:
    print("dir already exists")

# to run without cmd-args, disable the above code and use the below line to give a directory to work with
# dir_name = "04b_test"


class Browser:
    def __init__(self, comm, visited, current, last_page):
        self.comm = comm
        self.visited = visited
        self.current = current
        self.last_page = last_page


    def get_input(self):
        print(Fore.WHITE + "Enter URL")
        self.comm = input()

        if self.comm == "exit":
            sys.exit()

        # add back functionality, which will do nothing is there's no page to go back to
        # if there are pages to go back to it checks if current site = last visited in stack
        # if it is it'll pop that entry and THEN load the last page in stack.
        # else it'll just directly get the last page from the stack.
        elif self.comm == "back":
            if not self.visited:
                self.get_input()
            else:
                if self.visited[-1] == self.current and len(self.visited) > 1:
                    self.visited.pop()
                    self.get_from_file(self.visited.pop())

                elif self.visited[-1] == self.current and len(self.visited) == 1:
                    self.get_input()
                else:
                    self.get_from_file(self.visited.pop())
        else:
            self.check_input(self.comm)



    def check_input(self, to_check):

        # google
        if to_check in self.visited:
            self.get_from_file(self.comm)

        # google.com
        elif to_check[:-3] in self.visited:
            self.get_from_file(self.comm[:-3])
        elif to_check[:-3] not in self.visited:
            site = 'https://' + to_check
            file = to_check[:-3]
            self.first_visit(site, file)

        # http://google.com
        elif to_check.startswith('http://'):
            file = to_check[7:-4]
            if file in self.visited:
                self.get_from_file(to_check)
            else:
                self.first_visit(to_check, file)

        # httpS://google.com
        elif to_check.startswith('https://'):
            file = to_check[8:-4]
            if file in self.visited:
                self.get_from_file(to_check)
            else:
                self.first_visit(to_check, file)


    def first_visit(self, site, file):
        try:
            req = requests.get(site)
            soup = BeautifulSoup(req.content, 'html.parser')
            all_tags = soup.find_all(['p', 'h1', 'h2', 'a', 'ul', 'ol', 'li'])
            for ea in all_tags:
                if ea.name == "a":
                    print(Fore.BLUE + ea.text)
                else:
                    print(Fore.WHITE + ea.text)

            to_write = f"{dir_name}/{file}"
            with open(to_write, 'w', encoding='utf-8') as write_site:
                self.current = file
                for line in all_tags:
                    if line.name == "a":
                        write_site.write(Fore.BLUE + line.text + "\n")
                    else:
                        write_site.write(Fore.WHITE + line.text + "\n")
                self.add_to_que(file)
            self.get_input()
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
            print("Error: Invalid URL")
            self.get_input()


    def get_from_file(self, file):
        to_open = f"{dir_name}/{file}"
        self.current = file
        with open(to_open, 'r', encoding='utf-8') as read_site:
            print(read_site.read())
            self.add_to_que(file)
        self.get_input()


    def add_to_que(self, file):
        self.visited.append(file)
        self.current = file


if __name__ == "__main__":
    instance = Browser("", [], "", [])
    print("""
Enter a URL to browse the interwebs.
You can also use 'back' to go back to the previous pages or 'exit' to exit.
Every site you visit will be saved in a 'cache', represented by a txt-file in the dir created.
""")
    instance.get_input()
