import requests
from connection.connection_variables import link
from parameters.subscription.case_4.subscription_params import *


def case_four_subscription():
    return requests.get(link, case_4_first_subscription_params)

