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

# case_two_first_subscription()
# case_two_second_subscription()
case_two_third_subscription()
# case_two_fourth_subscription()
# case_two_fifth_subscription()
# case_two_sixth_subscription()
# case_two_seventh_subscription()