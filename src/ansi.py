
class AnsiValues:
    CSI             = '\033['

def code_to_chars(code):
    return AnsiValues.CSI + str(code) + 'm'

class AnsiCodes(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))

class AnsiFore(AnsiCodes):
    RESET           = 0

    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37

    LIGHTBLACK      = 90
    LIGHTRED        = 91
    LIGHTGREEN      = 92
    LIGHTYELLOW     = 93
    LIGHTBLUE       = 94
    LIGHTMAGENTA    = 95
    LIGHTCYAN       = 96
    LIGHTWHITE      = 97

Fore                = AnsiFore()