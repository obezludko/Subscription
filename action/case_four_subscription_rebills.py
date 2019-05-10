import requests
from connection.connection_variables import link_for_rebill
from parameters.subscription.case_4.subscription_params import *
from parameters.rebill.case_4.rebill_params import *


def case_four_subscription():
    return requests.get(link_for_rebill, case_4_first_subscription_params)


def case_four_first_rebill():
    return requests.get(link_for_rebill, case_4_first_rebill_params)

def case_four_second_rebill():
    return requests.get(link_for_rebill, case_4_second_rebill_params)



