import requests
from connection.connection_variables import link
from parameters.subscription.case_3.subscription_params import *


def case_three_first_subscription():
    return requests.get(link,case_3_first_subscription_params)

