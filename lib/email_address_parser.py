import re

# your code goes here!
class EmailAddressParser:
    def __init__(self, emails_string):
        self.emails_string = emails_string

    def parse(self):
        emails = re.split(r"\s+|,", self.emails_string)

        email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
        valid_emails = [email for email in reversed(emails) if email_pattern.match(email)]

        return valid_emails
    

parser1 = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
print(parser1.parse())
parser2 = EmailAddressParser("talk@talk.com,john.jones@flatironschool.com,alexa@amazon.com")
print(parser2.parse())
parser3 = EmailAddressParser("talk@talk.com, john.jones@flatironschool.com, alexa@amazon.com")
print(parser3.parse())
parser4 = EmailAddressParser("talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why")
print(parser4.parse())