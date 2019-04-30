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
 Сравнивается с типом коэффициента, по которому была созданна подписка. 
 После этого коэффициент, который был закрыт до этого(строка 80) открывается,
  для создания последующей подписки с ребиллами"""
if save_second_rebill[13] == save_user_offer_coefficient[3]:
    print("Second rebill user_coefficient_type({}) = subscription user_coefficient_type({})".format(save_second_rebill[13],save_user_offer_coefficient[3]))
else:
    print("Second rebill user_coefficient_type({}) != subscription user_coefficient_type({})".format(save_second_rebill[13],save_user_offer_coefficient[3]))

if save_user_offer_coefficient[6] != None:
    print("Check coeffisient status.\nCoefficient is closed.\nCoefficient opening.")
    time.sleep(3)
    open_user_offer_coefficient()
    print("Coefficient is opened")
else:
    print("Coefficient is opened. Do nothing")


"""Second subscription block.
 Create and select second subscription"""
def select_created_second_subscription():
    case_four_second_subscription()
    time.sleep(3)
    cursor = connection.cursor()
    second_subscription_select_query = "SELECT * " \
                                "FROM subscription " \
                                "WHERE click_id = {} " \
                                "AND external_subscription_id = '{}'".format(used_click_for_subscription,
                                                                             case_4_second_subscription_params["external_subscription_id"])
    cursor.execute(second_subscription_select_query)
    second_subscription_cortage = cursor.fetchall()
    subscription_row = second_subscription_cortage[0]
    return subscription_row


"""Save selected second subscription data into variable"""
save_second_subscription_parameters = select_created_second_subscription()


# ТУТ НУЖНО ДОБАВИТЬ БЛОК,
# ГДЕ БУДЕТ ЗАКРЫВАТЬСЯ ПРЕДЫДУЩИЙ КОЭФФИЦИЕНТ, А ПОСЛЕ ЭТОГО СОЗДАВАТЬСЯ НОВЫЙ

# INSERT INTO "public"."users_sms_offers_coefficient" ("id", "user_id", "sms_offer_id", "coefficient_type", "coefficient_value", "closed_at", "deleted_at", "created_at", "updated_at")
# VALUES (DEFAULT, 58, 453, 'percent', 0.4, null, null, '2019-04-30 14:54:46', null)





# print(save_subscription_parameters)
# print(save_second_subscription_parameters)
# close_user_offer_coefficient()
# open_user_offer_coefficient()
# offer_id = save_subscription_parameters[11]

