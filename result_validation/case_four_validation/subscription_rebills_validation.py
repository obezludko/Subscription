import psycopg2
import time
from action.case_four_subscription_rebills import *
from connection.connection_variables import pg_user, \
    pg_password, \
    pg_host, \
    pg_port, \
    pg_database
from parameters.subscription.case_4.subscription_params import *
# from parameters.rebill.case_4.

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
print(save_subscription_parameters)
