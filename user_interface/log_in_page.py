from screenpy.target import Target


WELCOME_MESSAGE = Target.the('welcome message').located_by('#GREET-HELLO')
EMAIL_INPUT = Target.the('email input').located_by('#userid')
PASSWORD_INPUT = Target.the('password input').located_by('#pass')
LOGIN_BUTTON = Target.the('login.py button').located_by('#sgnBt')
LOG_IN_FAILED = Target.the('login.py failed').located_by('#errf')