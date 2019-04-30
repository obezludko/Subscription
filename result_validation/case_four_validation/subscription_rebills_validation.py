import psycopg2
import time
from action.case_four_subscription_rebills import *
from connection.connection_variables import pg_user, \
    pg_password, \
    pg_host, \
    pg_port, \
    pg_database
from parameters.subscription.case_4.subscription_params import *
from parameters.rebill.case_4.rebill_params import *

"""Connect to database using connection variables"""
connection = psycopg2.connect(database=pg_database,
                              user=pg_user,
                              password=pg_password,
                              host=pg_host,
                              port=pg_port)

def select_created_subscription():
    case_four_subscription()
    time.sleep(3)
    cursor = connection.cursor()
    subscription_select_query = "SELECT * " \
                                "FROM subscription " \
                                "WHERE click_id = {}".format(used_click_for_subscription)
    cursor.execute(subscription_select_query)
    subscription_cortage = cursor.fetchall()
    subscription_row = subscription_cortage[0]
    return subscription_row


"""Save selected subscription data into variable"""
save_subscription_parameters = select_created_subscription()



"""User_coefficient manipulation functions"""
def close_user_offer_coefficient():
    subscription_user_coefficient_id = save_subscription_parameters[12]
    cursor = connection.cursor()
    close_user_coefficient_query = "UPDATE users_sms_offers_coefficient " \
                             "SET deleted_at = now() " \
                             "WHERE id = {}".format(subscription_user_coefficient_id)
    cursor.execute(close_user_coefficient_query)
    connection.commit()
    return cursor.close()


def open_user_offer_coefficient():
    subscription_user_coefficient_id = save_subscription_parameters[12]
    cursor = connection.cursor()
    open_user_offer_coefficient_query = "UPDATE users_sms_offers_coefficient " \
                             "SET deleted_at = null " \
                             "WHERE id = {}".format(subscription_user_coefficient_id)
    cursor.execute(open_user_offer_coefficient_query)
    connection.commit()
    return cursor.close()


"""Create and save selected first rebill data into variable"""
def select_created_first_rebill():
    case_four_first_rebill()
    time.sleep(2)
    cursor = connection.cursor()
    first_rebill_select_query = "SELECT * " \
                                "FROM rebill " \
                                "WHERE click_id = {} AND external_message_id = '{}'".format(used_click_for_subscription,
                                                                                          case_4_first_rebill_params["external_message_id"])
    cursor.execute(first_rebill_select_query)
    first_rebill_cortage = cursor.fetchall()
    first_rebill_row = first_rebill_cortage[0]
    return first_rebill_row


save_first_rebill = select_created_first_rebill()


"""Close USER OFFER COEFFICIENT and create new rebill and select it"""
def select_created_second_rebill():
    close_user_offer_coefficient()  # Closing USER OFFER COEFFICIENT action
    case_four_second_rebill()
    time.sleep(3)
    cursor = connection.cursor()
    second_rebill_select_query = "SELECT * " \
                                "FROM rebill " \
                                "WHERE click_id = {} AND external_message_id = '{}'".format(used_click_for_subscription,
                                                                                          case_4_second_rebill_params["external_message_id"])
    cursor.execute(second_rebill_select_query)
    second_rebill_cortage = cursor.fetchall()
    second_rebill_row = second_rebill_cortage[0]
    return second_rebill_row

save_second_rebill = select_created_second_rebill()


# print(save_subscription_parameters)
# print(save_first_rebill)
# close_user_offer_coefficient()
# open_user_offer_coefficient()
# offer_id = save_subscription_parameters[11]



