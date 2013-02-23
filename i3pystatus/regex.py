import re

from i3pystatus import IntervalModule

class Regex(IntervalModule):
    """
    Simple regex file watcher
    """

    flags = 0
    format = "{0}"
    settings = (
        ("format", "format string used for output"),
        "regex",
        ("file", "file to search for regex matches"),
        ("flags", "Python.re flags"),
    )
    required = ("regex", "file")

    def init(self):
        self.re = re.compile(self.regex, self.flags)

    def run(self):
        with open(self.file, "r") as f:
            match = self.re.search(f.read())
            self.output = self.output = {
                "full_text" : self.format.format(*match.groups()),
            }