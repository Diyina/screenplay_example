from screenpy.questions import Text
from screenpy.pacing import beat

from ..user_interface import log_in_page


class Login_Failed_Message:
    @staticmethod
    def text():
        return Login_Failed_Message()

    @beat("check the error message...")
    def answered_by(self, actor):
        return Text.of(log_in_page.LOG_IN_FAILED).answered_by(actor)
