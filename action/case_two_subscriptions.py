import requests
from connection.connection_variables import link_for_rebill
from parameters.subscription.case_2.subscription_params import *


def case_two_first_subscription():
    return requests.get(link_for_rebill, case_2_first_subscription_params)


def case_two_second_subscription():
    return requests.get(link_for_rebill, case_2_second_subscription_params)


def case_two_third_subscription():
    return requests.get(link_for_rebill, case_2_third_subscription_params)


def case_two_fourth_subscription():
    return requests.get(link_for_rebill, case_2_fourth_subscription_params)


def case_two_fifth_subscription():
    return requests.get(link_for_rebill, case_2_fifth_subscription_params)


def case_two_sixth_subscription():
    return requests.get(link_for_rebill, case_2_sixth_subscription_params)


def case_two_seventh_subscription():
    return requests.get(link_for_rebill, case_2_seventh_subscription_params)
