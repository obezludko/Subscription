import psycopg2
from action.case_one_subscription_rebill_cancel import case_one_subscription, case_one_first_rebill
from connection.connection_variables import pg_user, \
    pg_password, \
    pg_host, \
    pg_port, \
    pg_database
from parameters.subscription.case_1.subsciption_params import used_click_for_subscription, \
    case_1_subscription_params
from parameters.rebill.case_1.rebill_params import case_1_first_rebill_params

"""Connect to database using connection variables"""
connection = psycopg2.connect(database=pg_database,
                              user=pg_user,
                              password=pg_password,
                              host=pg_host,
                              port=pg_port)

case_one_subscription()               # action subscription makes here
case_one_first_rebill()               # First rebill action makes here


def select_created_subscription():
    cursor = connection.cursor()
    subscription_select_query = 'SELECT * ' \
                                'FROM subscription ' \
                                'WHERE click_id = %s;' % used_click_for_subscription
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


if case_1_subscription_params['click_id'] == subscription_click_id():
    print('subscription_click_id true')
else:
    print('subscription_click_id false')

"""Select subscription_external_message_id and validate it after"""
def subscription_external_message_id():
    subscription_external_message_id = save_subscription_parameters[14]
    return str(subscription_external_message_id)


if case_1_subscription_params['external_message_id'] == subscription_external_message_id():
    print('subscription_external_message_id true')
else:
    print('subscription_external_message_id false')

"""Select gateway_id for validation after"""
def define_subscription_gateway_id():
    cursor = connection.cursor()
    gateway_select_query = "SELECT * " \
                           "FROM gateway_aliases " \
                           "WHERE alias = '{}'".format(case_1_subscription_params['partner'])
    cursor.execute(gateway_select_query)
    gateway_cortage = cursor.fetchall()
    gateway_parameters = gateway_cortage[0]
    gateway_id = gateway_parameters[2]
    return str(gateway_id)


"""Select subscription_gateway_id and validate it using previous selecting"""
def subscription_gateway_id():
    subscription_gateway_id = save_subscription_parameters[17]
    return str(subscription_gateway_id)


if define_subscription_gateway_id() == subscription_gateway_id():
    print('subscription_partner true')
else:
    print('subscription_partner false')

"""Select subscription_external_subscription_id and validate it"""
def subscription_external_subscription_id():
    subscription_external_subscription_id = save_subscription_parameters[2]
    return subscription_external_subscription_id


if case_1_subscription_params['external_subscription_id'] == subscription_external_subscription_id():
    print('subscription_external_subscription_id true')
else:
    print('subscription_external_subscription_id false')

"""Select extra_param and validate it"""
def select_extra_param():
    subscription_extra_param = save_subscription_parameters[15]
    return subscription_extra_param


if case_1_subscription_params['extra_param'] == select_extra_param():
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
    print('subscription closed_at true')
else:
    print('subscription closed_at false')


"""Validate is_hidden"""
if save_subscription_parameters[13] == False:
    print("Subscription is_hidden is checked. Test was passed")
else:
    print("Subscription is_hidden is checked. Test wasn't passed")


"""Validate subscription access_period"""
if save_subscription_parameters[10] == 0:
    print('Subscription access_period true')
else:
    print('Subscription access_period false')


"""Validate subscription is_hidden"""
if save_subscription_parameters[13] == False:
    print("Subscription is_hidden = False. Test was passed")
else:
    print("Subscription is_hidden = True. Test wasn't passed")



"""=====================================================================================
========================================================================================
========================================================================================
From this place we start validate first created rebill"""


def select_created_first_rebill():
    cursor = connection.cursor()
    first_rebill_select_query = "SELECT * " \
                                "FROM rebill " \
                                "WHERE click_id = {} AND external_message_id = '{}'".format(used_click_for_subscription,
                                                                                            case_1_first_rebill_params[
                                                                                                'external_message_id'])
    cursor.execute(first_rebill_select_query)
    first_rebill_cortage = cursor.fetchall()
    first_rebill_row = first_rebill_cortage[0]
    return first_rebill_row

"""Save selected first rebill data into variable"""
save_first_rebill = select_created_first_rebill()

"""Select click_id and validate it"""
def first_rebill_click_id():
    first_rebill_click_id = save_first_rebill[6]
    return str(first_rebill_click_id)

if case_1_first_rebill_params['click_id'] == first_rebill_click_id():
    print('first_rebill_click_id true')
else:
    print('first_rebill_click_id false')


"""Select gateway_id for validation after"""
def define_first_rebill_gateway_id():
    cursor = connection.cursor()
    gateway_select_query = "SELECT * " \
                           "FROM gateway_aliases " \
                           "WHERE alias = '{}'".format(case_1_first_rebill_params['partner'])
    cursor.execute(gateway_select_query)
    gateway_cortage = cursor.fetchall()
    gateway_parameters = gateway_cortage[0]
    gateway_id = gateway_parameters[2]
    return str(gateway_id)

def first_rebill_gateway_id():
    return str(save_first_rebill[2])

if  define_first_rebill_gateway_id() == first_rebill_gateway_id():
    print('first_rebill_gateway_id true')
else:
    print('first_rebill_gateway_id false')


"""Select first rebill external_message_id and validate it"""
def first_rebill_external_message_id():
    return save_first_rebill[10]

if case_1_first_rebill_params['external_message_id'] == first_rebill_external_message_id():
    print('first_rebill_external_message_id true')
else:
    print('first_rebill_external_message_id false')


"""Validate first rebill external_subscription_id"""
if case_1_first_rebill_params['external_subscription_id'] == subscription_external_subscription_id():
    print('First rebill external_subscription_id true')
else:
    print('First rebill external_subscription_id false')


"""Validate related with money parameters"""
def select_first_rebill_currency_rate():
    cursor = connection.cursor()
    select_currency_rate_query = "SELECT rate " \
                                 "FROM currency " \
                                 "WHERE code = '{}'".format(case_1_first_rebill_params['currency'])
    cursor.execute(select_currency_rate_query)
    rate_cortage = cursor.fetchall()
    first_rebill_row = rate_cortage[0]
    return first_rebill_row[0]

"""Calculate money_from_gateway using currency rate"""
def calculate_first_rebill_money_from_gateway_using_currency():
    calculate_payout = select_first_rebill_currency_rate() \
                       * float(case_1_first_rebill_params['payout'])
    return calculate_payout

"""Define user base coefficient"""
def select_first_rebill_user_base_coefficient():
    cursor = connection.cursor()
    select_user_base_coefficient = "SELECT base_coefficient " \
                                   "FROM \"user\" " \
                                   "WHERE id = {}".format(save_first_rebill[3])
    cursor.execute(select_user_base_coefficient)
    base_coefficient_cortage = cursor.fetchall()
    base_coefficient = base_coefficient_cortage[0]
    return base_coefficient[0]

"""Validate money_from_gateway"""
if calculate_first_rebill_money_from_gateway_using_currency() == float(case_1_first_rebill_params['payout']) * select_first_rebill_currency_rate():
    print('First rebill money_from_gateway true')
else:
    print('First rebill money_from_gateway false')


def select_first_rebill_is_payout_received():
    cursor = connection.cursor()
    select_is_payout_received = "SELECT is_payout_received " \
                                "FROM rebill " \
                                "WHERE click_id = {} " \
                                "AND external_message_id = '{}'".format(used_click_for_subscription,
                                                                        case_1_first_rebill_params[
                                                                            'external_message_id'])
    cursor.execute(select_is_payout_received)
    is_payout_received_cortage = cursor.fetchall()
    is_payout_received = is_payout_received_cortage[0]
    return is_payout_received[0]


def check_key_value():
    is_payout = 'payout' in case_1_first_rebill_params
    return is_payout


if select_first_rebill_is_payout_received() == check_key_value():
    print('First rebill is_payout_received true')
else:
    print('First rebill is_payout_received false')


if save_first_rebill[17] == case_1_first_rebill_params['extra_param']:
    print('First rebill extra_param true')
else:
    print('First rebill extra_param false')


"""Validate user role"""
def select_first_rebill_user_role():
    cursor = connection.cursor()
    select_user_role = "SELECT role " \
                       "FROM \"user\" " \
                       "WHERE id = {}".format(save_first_rebill[3])
    cursor.execute(select_user_role)
    user_role_cortage = cursor.fetchall()
    user_role = user_role_cortage[0]
    return user_role[0]

if select_first_rebill_user_role() == save_first_rebill[18]:
    print('First rebill user_role true')
else:
    print('First rebill user_role false')


