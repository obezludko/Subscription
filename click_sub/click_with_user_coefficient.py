import requests
from click_sub.subs_generator import generate_sub
from urllib.parse import urlparse

subs = {'sub2': generate_sub('SuB2'),
        'sub1': generate_sub('sUb1'),
        'sub3': generate_sub('SSub3'),
        'sub4': generate_sub('suBB4'),
        'sub5': generate_sub('sub5')
        }

link_with_user_coefficient = 'http://159.69.25.152/go?id=736&hash=_QHPI-t7FC'


"""Send request using link variables and generated in subs_generator subs.
After that get parsed response url and separate it on params and get click_id from there"""

def get_click_id_from_responce():
    request = requests.get(link_with_user_coefficient, subs)
    parsed_url = urlparse(request.text)
    click_id = parsed_url.path[1:]
    return click_id
