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
    print('click_id true')
else:
    print('click_id false')

"""Select subscription_external_message_id and validate it after"""
def subscription_external_message_id():
    subscription_external_message_id = save_subscription_parameters[14]
    return str(subscription_external_message_id)


if case_1_subscription_params['external_message_id'] == subscription_external_message_id():
    print('external_message_id true')
else:
    print('external_message_id false')

"""Select gateway_id for validation after"""
def select_gateway_id():
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


if select_gateway_id() == subscription_gateway_id():
    print('partner true')
else:
    print('partner false')

"""Select subscription_external_subscription_id and validate it"""
def subscription_external_subscription_id():
    subscription_external_subscription_id = save_subscription_parameters[2]
    return subscription_external_subscription_id


if case_1_subscription_params['external_subscription_id'] == subscription_external_subscription_id():
    print('external_subscription_id true')
else:
    print('external_subscription_id false')

"""Select extra_param and validate it"""
def select_extra_param():
    subscription_extra_param = save_subscription_parameters[15]
    return subscription_extra_param


if case_1_subscription_params['extra_param'] == select_extra_param():
    print('extra_param true')
else:
    print('extra_param false')


"""First rebill validation makes here"""
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

"""Save selected subscription data into variable"""
save_first_rebill = select_created_first_rebill()


def first_rebill_click_id():
    first_rebill_click_id = save_first_rebill[6]
    return str(first_rebill_click_id)

if case_1_first_rebill_params['click_id'] == first_rebill_click_id():
    print('first_rebill_click_id true')
else:
    print('first_rebill_click_id false')


# print(first_rebill_click_id())