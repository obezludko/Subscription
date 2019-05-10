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
                                "WHERE click_id = {} " \
                                "AND external_subscription_id = '{}'".format(used_click_for_subscription,
                                                                             case_4_first_subscription_params["external_subscription_id"])
    cursor.execute(subscription_select_query)
    subscription_cortage = cursor.fetchall()
    subscription_row = subscription_cortage[0]
    return subscription_row


"""Save selected subscription data into variable"""
save_subscription_parameters = select_created_subscription()


"""Select subscription_click_id and validate it after"""
def subscription_click_id():
    subscription_click_id = save_subscription_parameters[3]
    return str(subscription_click_id)


if case_4_first_subscription_params["click_id"] == subscription_click_id():
    print("subscription_click_id true")
else:
    print("subscription_click_id false")

"""Validate subscription_external_message_id"""
if case_4_first_subscription_params["external_message_id"] == str(save_subscription_parameters[14]):
    print('subscription_external_message_id true')
else:
    print('subscription_external_message_id false')


"""Select gateway_id for validation after"""
def define_subscription_gateway_id():
    cursor = connection.cursor()
    gateway_select_query = "SELECT * " \
                           "FROM gateway_aliases " \
                           "WHERE alias = '{}'".format(case_4_first_subscription_params['partner'])
    cursor.execute(gateway_select_query)
    gateway_cortage = cursor.fetchall()
    gateway_parameters = gateway_cortage[0]
    gateway_id = gateway_parameters[2]
    return str(gateway_id)


if define_subscription_gateway_id() == str(save_subscription_parameters[17]):
    print('subscription_partner true')
else:
    print('subscription_partner false')


"""Validate subscription_external_subscription_id"""
if case_4_first_subscription_params["external_subscription_id"] == save_subscription_parameters[2]:
    print('subscription_external_subscription_id true')
else:
    print('subscription_external_subscription_id false')


"""Select extra_param and validate it"""
if case_4_first_subscription_params["extra_param"] == save_subscription_parameters[15]:
    print('subscription_extra_param true')
else:
    print('subscription_extra_param false')


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
    print("subscription_user_role true")
else:
    print("subscription_user_role false")


"""Validate closed_at"""
if save_subscription_parameters[7] == None:
    print('subscription is opened. Test was passed')
else:
    print('subscription is closed. Test was failed')


"""Validate is_hidden"""
def select_user_offer_coefficient_type():
    subscription_user_coefficient_id = save_subscription_parameters[12]
    cursor = connection.cursor()
    select_user_offer_coefficient_type_query = "SELECT coefficient_type " \
                                                        "FROM users_sms_offers_coefficient " \
                                                        "WHERE id = {}".format(subscription_user_coefficient_id)
    cursor.execute(select_user_offer_coefficient_type_query)
    second_rebill_user_offer_coefficient_cortage = cursor.fetchall()
    second_rebill_user_offer_coefficient = second_rebill_user_offer_coefficient_cortage[0]
    return second_rebill_user_offer_coefficient[0]

coefficient_type = select_user_offer_coefficient_type()
cpa_list = ["cpa_sub", "cpa_rebill"]

if (coefficient_type not in cpa_list) and save_subscription_parameters[13] == False:
    print("{} NOT IN {}. Test was passed. is_hidden = {}. Test was passed".format(coefficient_type, cpa_list,
                                                                                  save_subscription_parameters[13]))
else:
    print("{} IN {}. Test was failed. \nis_hidden = {}. Test was failed".format(coefficient_type, cpa_list,
                                                                                save_subscription_parameters[13]))

################ Я остановился тут
################

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


"""Check and save user_offer_coefficient status"""
def select_second_rebill_user_offer_coefficient():
    subscription_user_coefficient_id = save_subscription_parameters[12]
    cursor = connection.cursor()
    select_second_rebill_user_offer_coefficient_query = "SELECT * " \
                                                        "FROM users_sms_offers_coefficient " \
                                                        "WHERE id = {}".format(subscription_user_coefficient_id)
    cursor.execute(select_second_rebill_user_offer_coefficient_query)
    second_rebill_user_offer_coefficient_cortage = cursor.fetchall()
    second_rebill_user_offer_coefficient = second_rebill_user_offer_coefficient_cortage[0]
    return second_rebill_user_offer_coefficient

save_user_offer_coefficient = select_second_rebill_user_offer_coefficient()

"""Проверка типа коэффициента второго ребилла.
 Сравнивается с типом коэффициента, по которому была созданна подписка. """
if save_second_rebill[13] == save_user_offer_coefficient[3]:
    print("Second rebill user_coefficient_type({}) = subscription user_coefficient_type({})".format(save_second_rebill[13],save_user_offer_coefficient[3]))
else:
    print("Second rebill user_coefficient_type({}) != subscription user_coefficient_type({})".format(save_second_rebill[13],save_user_offer_coefficient[3]))

if save_user_offer_coefficient[6] != None:
    print("Check coefficient status.\nCoefficient is closed.\nCoefficient opening.")
    time.sleep(3)
    open_user_offer_coefficient()
    print("Coefficient is opened")
else:
    print("Coefficient is opened. Do nothing")



# INSERT INTO "public"."users_sms_offers_coefficient" ("id", "user_id", "sms_offer_id", "coefficient_type", "coefficient_value", "closed_at", "deleted_at", "created_at", "updated_at")
# VALUES (DEFAULT, 58, 453, 'percent', 0.4, null, null, '2019-04-30 14:54:46', null)





# print(save_subscription_parameters)
# print(save_second_subscription_parameters)
# close_user_offer_coefficient()
# open_user_offer_coefficient()
# offer_id = save_subscription_parameters[11]

