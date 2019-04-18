import psycopg2
import time
from action.case_three_subscription_rebills import *
from connection.connection_variables import pg_user,\
    pg_password, \
    pg_host, \
    pg_port, \
    pg_database
from parameters.subscription.case_3.subscription_params import *


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


if define_subscription_gateway_id() == str(save_subscription_parameters[17]):
    print("Subscription partner true.")
else:
    print("Subscription partner false")


"""Validate external_subscription_id"""
if case_3_first_subscription_params["external_subscription_id"] == save_subscription_parameters[2]:
    print("external_subscription_id true")
else:
    print("external_subscription_id false")


"""Select subscription extra_param and validate it"""
if case_3_first_subscription_params["extra_param"] == save_subscription_parameters[15]:
    print("Subscription extra_param true")
else:
    print("Subscription extra_param false")


"""Select and validate subscription user_role"""
def select_subscription_user_role():
    cursor = connection.cursor()
    select_subscription_user_role = "SELECT role " \
                                    "FROM \"user\" " \
                                    "WHERE id = {}".format(save_subscription_parameters[18])
    cursor.execute(select_subscription_user_role)
    subscription_user_role_cortage = cursor.fetchall()
    subscription_user_role = subscription_user_role_cortage[0]
    return subscription_user_role[0]

if select_subscription_user_role() == save_subscription_parameters[16]:
    print("Subscription user_role true")
else:
    print("Subscription user_role false")

"""Check closed_at field"""
if save_subscription_parameters[7] == None:
    print("Subscription is opened. Test passed")
else:
    print("Subscription is closed. Test passed")


"""Validate subscription is_hiden"""
if save_subscription_parameters[13] == False:
    print("Subscription is hidden = false. Test was passed")
else:
    print("Subscription is_hidden = true. Test was passed")


"""
========================================================================================
From this place we validate rebills, that hasn't create
========================================================================================
"""

case_three_first_rebill()
# case_three_second_rebill()
# case_three_third_rebill()
# case_three_fourth_rebill()
# case_three_fifth_rebill()
# case_three_sixth_rebill()
# case_three_seventh_rebill()
# case_three_eighth_rebill()
# case_three_ninth_rebill()
