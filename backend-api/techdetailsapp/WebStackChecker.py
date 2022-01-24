
import builtwith


class WebStackChecker(object):

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f' Website - {self} tech stack -'

    def techStack(self):
        stackDetails = builtwith.parse(self.url)
        return stackDetails
