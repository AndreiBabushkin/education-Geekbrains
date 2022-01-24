import re

RE_IMAIL = re.compile(r'^\S+@[a-z]+[.][a-z]+$')

def email_parse(email_address):


    if RE_IMAIL.match(email_address):
        email_address = email_address.split('@')
        print({'username': email_address[0], 'domain': email_address[1]})
    else:
        msg = 'wrong email: ' + email_address
        raise ValueError(msg)


email_parse('junior088@iloud.com')