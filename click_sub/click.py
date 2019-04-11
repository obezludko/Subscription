import requests
from click_sub.subs_generator import generate_sub
from urllib.parse import urlparse

subs = {'sub2': generate_sub('SuB2'),
        'sub1': generate_sub('sUb1'),
        'sub3': generate_sub('SSub3'),
        'sub4': generate_sub('suBB4'),
        'sub5': generate_sub('sub5')
        }

link = 'http://159.69.25.152/go?id=735&hash=TvRcta7Cvh'

"""Send request using link variables and generated in subs_generator subs"""


def get_responce_url():
    request = requests.get(link, subs)
    return request.text


"""Get parsed response url and separate it on params and get click_id from there"""

def parse_url_and_append_click():
    url_response = get_responce_url()
    parsed_url = urlparse(url_response)
    click_id = parsed_url.path[1:]
    return click_id


# print(type(parse_url_and_append_click()))