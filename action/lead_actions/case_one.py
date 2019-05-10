import requests
from connection.connection_variables import link_for_lead
from parameters.lead.case_1.lead_params import *


def case_one_lead():
    return requests.get(link_for_lead,case_1_first_lead_params)

