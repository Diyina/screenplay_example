from screenpy.actions import Click, Enter
from ..user_interface.home_page import LOG_IN_LINK
from ..user_interface.log_in_page import (
    EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON
)


class Login(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def perform_as(self, actor):
        actor.attempts_to(Click.on_the(LOG_IN_LINK).then_wait_for(EMAIL_INPUT),
                          Enter.the_text(self.email).into_the(EMAIL_INPUT),
                          Enter.the_text(self.password).into_the(PASSWORD_INPUT),
                          Click.on_the(LOGIN_BUTTON))

    @staticmethod
    def using_credentials(email, password):
        return Login(email, password)
