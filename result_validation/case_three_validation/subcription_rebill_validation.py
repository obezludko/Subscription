import psycopg2
import time
from action.case_three_subscription_rebills import *
from connection.connection_variables import pg_user,\
    pg_password, \
    pg_host, \
    pg_port, \
    pg_database
from parameters.subscription.case_3.subscription_params import \
    used_click_for_subscription, case_3_first_subscription_params


"""Connect to database using connection variables"""
connection = psycopg2.connect(database=pg_database,
                              user=pg_user,
                              password=pg_password,
                              host=pg_host,
                              port=pg_port)

case_three_first_subscription()  # Action subscription makes here

"""Define sleeping time"""
define_sleep = time.sleep(2)

def select_created_subscription():
    cursor = connection.cursor()
    subscription_select_query = "SELECT * " \
                                "FROM subscription " \
                                "WHERE click_id ={}".format(used_click_for_subscription)
    cursor.execute(subscription_select_query)
    subscription_cortage = cursor.fetchall()
    subscription_row = subscription_cortage[0]
    return subscription_row

"""Save selected subscription data into variable"""
save_subscription_parameters = select_created_subscription()

"""Validate subscription click_id"""
if case_3_first_subscription_params['click_id'] == str(used_click_for_subscription):
    print("Subscription click_id true")
else:
    print("Subscription click_id false")


"""Validate subscription external_message_id"""
if case_3_first_subscription_params["external_message_id"] == str(save_subscription_parameters[14]):
    print('Subscription_external_message_id true')
else:
    print("Subscription_external_message_id true")


"""Select gateway_id for validation after"""
def define_subscription_gateway_id():
    cursor = connection.cursor()
    gateway_select_query = "SELECT gateway_id " \
                           "FROM gateway_aliases " \
                           "WHERE alias = '{}'".format(case_3_first_subscription_params["partner"])
    cursor.execute(gateway_select_query)
    gateway_id_cortage = cursor.fetchall()
    gateway_id = gateway_id_cortage[0]
    return str(gateway_id[0])

a = define_subscription_gateway_id()
print(type(a))