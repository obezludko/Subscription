import requests
from connection.connection_variables import link
from parameters.subscription.case_3.subscription_params import *


def case_three_first_subscription():
    return requests.get(link, case_3_first_subscription_params)


def case_three_first_rebill():
    return requests.get(link, case_3_first_rebill_params)


def case_three_second_rebill():
    return requests.get(link, case_3_second_rebill_params)


def case_three_third_rebill():
    return requests.get(link, case_3_third_rebill_params)


def case_three_fourth_rebill():
    return requests.get(link, case_3_fourth_rebill_params)


def case_three_fifth_rebill():
    return requests.get(link, case_3_fifth_rebill_params)


def case_three_sixth_rebill():
    return requests.get(link, case_3_sixth_rebill_params)


def case_three_seventh_rebill():
    return requests.get(link, case_3_seventh_rebill_params)


def case_three_eighth_rebill():
    return requests.get(link, case_3_eighth_rebill_params)


def case_three_ninth_rebill():
    return requests.get(link, case_3_ninth_rebill_params)
