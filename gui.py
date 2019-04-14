from htmlParse import Parser
from Main import ParseEpisodes
import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.text import Label as CoreLabel
from kivy.properties import StringProperty
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


# ----Docs-----
# https://kivy.org/doc/stable/
# https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html
# -------------
# https://stackoverflow.com/questions/51987320/pass-variables-from-py-to-kv-file
# https://www.youtube.com/watch?v=WdcUg_rX2fMs
# https://pythontips.com/2013/12/02/kivy-101-how-to-use-boxlayouts/

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widtget(self.password)

class Main_window(Widget):

    # def __init__(self, **kwargs):
    #     super(Main_window, self).__init__(**kwargs)
    #     layout = BoxLayout(orientation='vertical')
    #     my_label = CoreLabel()
        # my_label.text = 'hello'
        # layout.add_widget(my_label)
    pass

class ScreenManagement(ScreenManager):
    pass

Builder.load_string("""
""")

class ScrollableLabel(ScrollView):
    text = StringProperty("This is a test string 1 2 3 :: " * 20)

class HomeScreen(Screen):

    def get_episode_data(self):
        self.m = ParseEpisodes()
        self.m.parse()
        self.all_episodes = self.m.get_all()
        return self.all_episodes

    def show_tasks(self):
        self.all_episodes = self.get_episode_data()
        tasks = ["task 1", "task 2", "task 3", "task 4"]
        for episode in self.all_episodes:
            self.label_text = ""
            for k,v in episode.items():
                self.label_text += k + " " + v + "\n"
            self.grid.add_widget(Label(text=self.label_text))

class EpisodeApp(App):

    s = StringProperty("test string one")

    def build(self):
        # return ScrollableLabel()
        g = HomeScreen()
        g.show_tasks()
        return g


if __name__ == '__main__':
    EpisodeApp().run()















#
