import psycopg2
import time
from action.case_two_subscriptions import *
from connection.connection_variables import pg_user, \
    pg_password, \
    pg_host, \
    pg_port, \
    pg_database
from parameters.subscription.case_2.subscription_params import *

"""Connect to database using connection variables"""
connection = psycopg2.connect(database=pg_database,
                              user=pg_user,
                              password=pg_password,
                              host=pg_host,
                              port=pg_port)

"""Run negative GET requests, that have't create any subscriptions. 
After running define sleep time. Trying to select something after that."""
def select_uncreated_subscription():
    case_two_first_subscription()
    case_two_second_subscription()
    case_two_third_subscription()
    case_two_fourth_subscription()
    case_two_fifth_subscription()
    case_two_sixth_subscription()
    case_two_seventh_subscription()
    time.sleep(4)
    cursor = connection.cursor()
    subscription_select_query = "SELECT * " \
                                "FROM subscription " \
                                "WHERE click_id = {} " \
                                "OR (external_message_id = '{}' " \
                                "AND external_subscription_id = '{}')".format(used_click_for_subscription,
                                                                              case_2_second_subscription_params[
                                                                                  'external_message_id'],
                                                                              case_2_second_subscription_params[
                                                                                  'external_subscription_id'])
    cursor.execute(subscription_select_query)
    subscription_cortage = cursor.fetchall()
    return subscription_cortage

if select_uncreated_subscription() == []:
    print('Nothing is created. Test is passed.')
else:
    print('Something is created. Test is failed.')