from unittest import TestCase
from screenpy import AnActor
from screenpy.abilities import BrowseTheWeb
from selenium.webdriver import Chrome
from ..tasks.start import Start
from ..tasks.login import Login
from screenpy.actions import Wait
from ..questions.login_failed_message import Login_Failed_Message
from screenpy.resolutions import ContainsTheText

from ..user_interface import log_in_page as locators


class LoginFailedEbay(TestCase):

    def setUp(self):
        self.actor = AnActor.named('Anna').who_can(BrowseTheWeb.using(Chrome()))

    def tests_log_in_failed(self):
        Actor = self.actor
        Actor.was_able_to(Start.on_the_homepage())
        Actor.was_able_to(Login.using_credentials('hola@hola.com', '12345678'))
        Actor.was_able_to(Wait.for_the(locators.LOG_IN_FAILED).to_appear())
        Actor.should_see_that((Login_Failed_Message.text(), ContainsTheText('La información no coincide')))

    def tearDown(self):
        self.actor.exit_stage_right()
