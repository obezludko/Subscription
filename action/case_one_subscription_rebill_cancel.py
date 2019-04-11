import requests
from connection.connection_variables import link
from parameters.subscription.case_1.subsciption_params import *
from parameters.rebill.case_1.rebill_params import *
from parameters.cancel.case_1.cancel_params import *


def case_one_subscription():
    return requests.get(link, case_1_subscription_params)


def case_one_first_rebill():
    return requests.get(link, case_1_first_rebill_params)


def case_one_second_rebill():
    return requests.get(link, case_1_second_rebill_params)


def case_one_third_rebill():
    return requests.get(link, case_1_third_rebill_params)


def case_one_fourth_rebill():
    return requests.get(link, case_1_fourth_rebill_params)


def case_one_cancel():
    return requests.get(link, case_1_cancel_params)


