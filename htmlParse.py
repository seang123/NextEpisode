# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests, sys

# related to sorting
# https://www.geeksforgeeks.org/python-sort-list-of-dates-given-as-strings/

class Parser:
    def __init__(self, url):
        self.url = url

    def parse(self):
        self.get_next_ep()
        try:
            self.clean_next_ep()
            self.fail = False
        except:
            # if no episode info is available
            self.fail = True


    def is_fail(self):
        """true if episode info failed to be properly parsed"""
        return self.fail

    def fail_condition(self):
        """TODO: return the reason for failure"""
        return self.fail_condition

    def get_next_ep(self):
        """
        Downloads the pages html code
        Gets the title, and the next episode data
        """
        # https://next-episode.net/game-of-thrones
        page = requests.get(self.url)
        assert page.status_code == 200
        soup = BeautifulSoup(page.content, 'html.parser')
        self.title = str(soup.title.string).split(" - ")[0]
        self.next_ep = soup.find("div", {"id": "next_episode"})

    def clean_next_ep(self):
        """
        Given the next episode html data, take the relevent parts and put
        them into a dictionary
        """
        # keys holds the field names
        # keys = self.next_ep.find_all(class_="subheadline")

        # values holds episode name, number, and summary(ignore)
        name_number = self.next_ep.find_all(class_="sub_main")

        # gets: countdown, date, season
        self.cds = []
        for tag in self.next_ep:
            if tag.string is not None:
                s = str(tag.string).strip()
                # cds.append(" ".join(s.split()))
                self.cds.append(s)

        # removes the weird empty spaces that come from the raw html
        self.cds = [c for c in self.cds if c is not '']
        # adds the episode name and number to the list
        self.cds[0] = "Name:"
        self.cds.insert(1, name_number[0].string)
        self.cds.append("Episode:")
        self.cds.append(name_number[1].string)
        self.cds.insert(0, "")
        self.cds.insert(1, self.title)

        # converts the list to a dictionary for easier outputing
        self.cds = dict(zip(self.cds[::2], self.cds[1::2]))


    def get_date(self):
        return self.cds["Date:"]

    def get_output(self):
        """Returns the dictionary of info"""
        return self.cds

    def output_next_ep(self):
        """Returns the next episode data (currently just prints it)"""
        print(self.title)
        for k, v in self.cds.items():
            if k == 'Season:':
                print(v + " / " + self.cds["Episode:"])
                break;
            print(v)
