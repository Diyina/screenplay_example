from screenpy.actions import Open
from ..user_interface import home_page


class Start:
    @staticmethod
    def on_the_homepage():
        return Start(home_page.url)

    def perform_as(self, actor):
        actor.attempts_to(Open.browser_on(self.location))

    def __init__(self, location):
        self.location = location

