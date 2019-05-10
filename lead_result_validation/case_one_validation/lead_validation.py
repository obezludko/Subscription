import psycopg2
import time
from action.lead_actions.case_one import *
from connection.connection_variables import pg_user, \
    pg_password, \
    pg_host, \
    pg_port, \
    pg_database
from parameters.lead.case_1.lead_params import *

"""Connect to database using connection variables"""
connection = psycopg2.connect(database=pg_database,
                              user=pg_user,
                              password=pg_password,
                              host=pg_host,
                              port=pg_port)


def select_uncreated_leads():
    case_one_first_lead()
    case_one_second_lead()
    case_one_third_lead()
    case_one_fourth_lead()
    case_one_fifth_lead()
    case_one_sixth_lead()
    case_one_seventh_lead()
    case_one_eighth_lead()
    case_one_ninth_lead()
    case_one_tenth_lead()
    case_one_eleventh_lead()
    time.sleep(7)
    cursor = connection.cursor()
    lead_select_query = "SELECT * " \
                        "FROM lead " \
                        "WHERE click_id = {} " \
                        "OR external_message_id IN ('{}','{}','{}')".format(used_click_for_lead,
                                                                            case_1_sixth_lead_params['text_uniq_lead'],
                                                                            case_1_eighth_lead_params['text_uniq_lead'],
                                                                            case_1_ninth_lead_params['text_uniq_lead'],
                                                                            case_1_tenth_lead_params['text_uniq_lead'])
    cursor.execute(lead_select_query)
    lead_cortage = cursor.fetchall()
    return lead_cortage

if select_uncreated_leads() == []:
    print('Nothing was created. Test is passed.')
else :
    print("Something was created. Test isn't passed")