from htmlParse import Parser
from datetime import datetime

class ParseEpisodes:

    def __init__(self):
        self.shows = ["https://next-episode.net/game-of-thrones",
            "https://next-episode.net/brooklyn-nine-nine",
            "https://next-episode.net/lucifer",
            "https://next-episode.net/the-blacklist",
            "https://next-episode.net/izombie",
            "https://next-episode.net/archer", # currently breaks
            "https://next-episode.net/seal-team",
            "https://next-episode.net/s.w.a.t.",
            "https://next-episode.net/blindspot"]

    def parse(self):
        """
        Main method: parses the data and sorts it.
        """
        self.create_parse_object()

        """Currently first removing fails and then sorting doesn't work since
        during the removal I add a set stating which episode has failed
            So temporarly it may fix the issue to first sort and then remove.
        """
        self.remove_fails()
        self.sort()

    def get_all(self):
        """
            Returns a list of dictionaries containing each episodes data.
            The list is sorted by release date
        """
        self.output = []
        for p in self.pp:
            self.output.append(p.get_output())
        return self.output

    def create_parse_object(self):
        """
        Creates the htmlParser objects:
            downloads the html data,
            returns a dictionary which holds a single episodes data
        """
        self.pp = []
        for show in self.shows:
            p = Parser(show)
            p.parse()
            self.pp.append(p)

    def remove_fails(self):
        """
        Removes the episodes from the list that failed to load.
        """
        for i in self.pp:
            print("type i : ", type(i))
            if i.is_fail():
                # print("No info available for > " + i.title)
                # self.pp.append({"Name:", i.title, "Info:", "No info available"})
                self.pp.remove(i)

    def sort(self):
        """
        Sorts the list of episodes by release date
        """
        self.pp.sort(key = lambda date: datetime.strptime(date.get_date(), '%a %b %d, %Y'))
        for p in self.pp:
            print("")
            p.output_next_ep()



m = ParseEpisodes()
m.parse()
x = m.get_all()
