import psycopg2
import time
from action.case_one_subscription_rebill_cancel import case_one_subscription,\
    case_one_first_rebill, \
    case_one_second_rebill, \
    case_one_third_rebill, \
    case_one_fourth_rebill
from connection.connection_variables import pg_user, \
    pg_password, \
    pg_host, \
    pg_port, \
    pg_database
from parameters.subscription.case_1.subsciption_params import used_click_for_subscription, \
    case_1_subscription_params
from parameters.rebill.case_1.rebill_params import case_1_first_rebill_params, \
    case_1_second_rebill_params, \
    case_1_third_rebill_params, case_1_fourth_rebill_params

"""Connect to database using connection variables"""
connection = psycopg2.connect(database=pg_database,
                              user=pg_user,
                              password=pg_password,
                              host=pg_host,
                              port=pg_port)

case_one_subscription()               # Action subscription makes here
case_one_first_rebill()               # First rebill action makes here
case_one_second_rebill()              # Second rebill action makes here
case_one_third_rebill()               # Third rebill action makes here
case_one_fourth_rebill()              # Fourth rebill action makes here

"""Define sleeping time"""
define_sleep = time.sleep(2)


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



"""
========================================================================================
========================================================================================
From this place we start validate first created rebill
"""


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

if define_first_rebill_gateway_id() == first_rebill_gateway_id():
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


"""Validate first rebill money_for partner"""
if round(float(calculate_first_rebill_money_from_gateway_using_currency() \
        * select_first_rebill_user_base_coefficient()),2) == round(float(save_first_rebill[5]),2):
    print("first rebill money_for partner true")
else:
    print("first rebill money_for partner false")


"""Validate first_rebill is_payout_received"""
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


def first_rebill_check_key_value():
    is_payout = 'payout' in case_1_first_rebill_params
    return is_payout


if select_first_rebill_is_payout_received() == first_rebill_check_key_value():
    print('First rebill is_payout_received = true. Test was passed')
else:
    print("First rebill is_payout_received = false. Test wasn't passed")

"""Validate first_rebill extra_param"""
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


"""
========================================================================================
========================================================================================
From this place we start validate second created rebill
"""

def select_created_second_rebill():
    cursor = connection.cursor()
    second_rebill_select_query = "SELECT * " \
                                "FROM rebill " \
                                "WHERE click_id = {} AND external_message_id = '{}'".format(used_click_for_subscription,
                                                                                            case_1_second_rebill_params[
                                                                                                'text_uniq_lead'])
    cursor.execute(second_rebill_select_query)
    second_rebill_cortage = cursor.fetchall()
    second_rebill_row = second_rebill_cortage[0]
    return second_rebill_row


"""Save selected second rebill data into variable"""
save_second_rebill = select_created_second_rebill()


"""Select second rebill click_id and validate it"""
def second_rebill_click_id():
    second_rebill_click_id = save_second_rebill[6]
    return str(second_rebill_click_id)

if case_1_second_rebill_params['click_id'] == second_rebill_click_id():
    print('second_rebill_click_id true')
else:
    print('second_rebill_click_id false')



"""Select second rebill gateway_id for validation after"""
def define_second_rebill_gateway_id():
    cursor = connection.cursor()
    gateway_select_query = "SELECT * " \
                           "FROM gateway_aliases " \
                           "WHERE alias = '{}'".format(case_1_second_rebill_params['partner'])
    cursor.execute(gateway_select_query)
    gateway_cortage = cursor.fetchall()
    gateway_parameters = gateway_cortage[0]
    gateway_id = gateway_parameters[2]
    return str(gateway_id)

def second_rebill_gateway_id():
    return str(save_second_rebill[2])

if define_second_rebill_gateway_id() == second_rebill_gateway_id():
    print('second_rebill_gateway_id true')
else:
    print('second_rebill_gateway_id false')


"""Validate second_rebill external_message_id(text_uniq_lead)"""
if case_1_second_rebill_params['text_uniq_lead'] == save_second_rebill[10]:
    print('second_rebill_external_message_id true')
else:
    print('second_rebill_external_message_id false')


"""Validate second rebill external_subscription_id"""
if case_1_second_rebill_params['subscr'] == save_subscription_parameters[2]:
    print('second rebill external_subscription_id true')
else:
    print('second rebill external_subscription_id false')


"""Validate related with second rebill's money parameters"""
def select_second_rebill_currency_rate():
    cursor = connection.cursor()
    select_currency_rate_query = "SELECT rate " \
                                 "FROM currency " \
                                 "WHERE code = '{}'".format(case_1_second_rebill_params['currency'])
    cursor.execute(select_currency_rate_query)
    rate_cortage = cursor.fetchall()
    second_rebill_row = rate_cortage[0]
    return second_rebill_row[0]


"""Calculate second rebill money_from_gateway using currency rate"""
def calculate_second_rebill_money_from_gateway_using_currency():
    calculate_payout = select_second_rebill_currency_rate() \
                       * float(case_1_second_rebill_params['payout'])
    return calculate_payout

"""Define second rebill user base coefficient"""
def select_second_rebill_user_base_coefficient():
    cursor = connection.cursor()
    select_user_base_coefficient = "SELECT base_coefficient " \
                                   "FROM \"user\" " \
                                   "WHERE id = {}".format(save_second_rebill[3])
    cursor.execute(select_user_base_coefficient)
    base_coefficient_cortage = cursor.fetchall()
    base_coefficient = base_coefficient_cortage[0]
    return base_coefficient[0]


"""Validate second rebill money_from_gateway"""
if calculate_second_rebill_money_from_gateway_using_currency() == \
        float(case_1_second_rebill_params['payout']) * select_second_rebill_currency_rate():
    print('second rebill money_from_gateway true')
else:
    print('second rebill money_from_gateway false')


"""Validate second rebill money_for partner"""
if round(float(select_second_rebill_user_base_coefficient()
               * calculate_second_rebill_money_from_gateway_using_currency()),2) \
        == round(float(save_second_rebill[5]),2):
    print("second rebill money_for partner true")
else:
    print("second rebill money_for partner false")


"""Validate second_rebill is_payout_received"""
def select_second_rebill_is_payout_received():
    cursor = connection.cursor()
    select_is_payout_received = "SELECT is_payout_received " \
                                "FROM rebill " \
                                "WHERE click_id = {} " \
                                "AND external_message_id = '{}'".format(used_click_for_subscription,
                                                                        case_1_second_rebill_params[
                                                                            'text_uniq_lead'])
    cursor.execute(select_is_payout_received)
    is_payout_received_cortage = cursor.fetchall()
    is_payout_received = is_payout_received_cortage[0]
    return is_payout_received[0]


def second_rebill_check_key_value():
    is_payout = 'payout' in case_1_second_rebill_params
    return is_payout


if select_second_rebill_is_payout_received() == second_rebill_check_key_value():
    print("second rebill is_payout_received = true. Test was passed")
else:
    print("second rebill is_payout_received = false. Test wasn't passed")


"""Validate second_rebill extra_param"""
if save_second_rebill[17] == case_1_second_rebill_params['extra_param']:
    print('second rebill extra_param true')
else:
    print('second rebill extra_param false')


"""Validate second rebill user role"""
def select_second_rebill_user_role():
    cursor = connection.cursor()
    select_user_role = "SELECT role " \
                       "FROM \"user\" " \
                       "WHERE id = {}".format(save_second_rebill[3])
    cursor.execute(select_user_role)
    user_role_cortage = cursor.fetchall()
    user_role = user_role_cortage[0]
    return user_role[0]

if select_second_rebill_user_role() == save_second_rebill[18]:
    print('second rebill user_role true')
else:
    print('second rebill user_role false')


"""
========================================================================================
========================================================================================
From this place we start validate third created rebill
"""


def select_created_third_rebill():
    cursor = connection.cursor()
    third_rebill_select_query = "SELECT * " \
                                "FROM rebill " \
                                "WHERE click_id = {} AND external_message_id = '{}'".format(used_click_for_subscription,
                                                                                            case_1_third_rebill_params[
                                                                                                'text_uniq_lead'])
    cursor.execute(third_rebill_select_query)
    third_rebill_cortage = cursor.fetchall()
    third_rebill_row = third_rebill_cortage[0]
    return third_rebill_row


"""Save selected third rebill data into variable"""
save_third_rebill = select_created_third_rebill()


"""Select third rebill click_id and validate it"""
def third_rebill_click_id():
    third_rebill_click_id = save_third_rebill[6]
    return str(third_rebill_click_id)

if case_1_third_rebill_params['click_id'] == third_rebill_click_id():
    print('third_rebill_click_id true')
else:
    print('third_rebill_click_id false')


"""Select third rebill gateway_id for validation after"""
def define_third_rebill_gateway_id():
    cursor = connection.cursor()
    gateway_select_query = "SELECT * " \
                           "FROM gateway_aliases " \
                           "WHERE alias = '{}'".format(case_1_third_rebill_params['partner'])
    cursor.execute(gateway_select_query)
    gateway_cortage = cursor.fetchall()
    gateway_parameters = gateway_cortage[0]
    gateway_id = gateway_parameters[2]
    return str(gateway_id)

def third_rebill_gateway_id():
    return str(save_third_rebill[2])

if define_third_rebill_gateway_id() == third_rebill_gateway_id():
    print('third_rebill_gateway_id true')
else:
    print('third_rebill_gateway_id false')


"""Validate third_rebill external_message_id(text_uniq_lead)"""
if case_1_third_rebill_params['text_uniq_lead'] == save_third_rebill[10]:
    print('third_rebill_external_message_id true')
else:
    print('third_rebill_external_message_id false')


"""Validate third rebill external_subscription_id(subscr)"""
if case_1_third_rebill_params['subscr'] == save_subscription_parameters[2]:
    print('third rebill external_subscription_id true')
else:
    print('third rebill external_subscription_id false')


"""Validate related with third rebill's money parameters"""
def select_third_rebill_currency_rate():
    cursor = connection.cursor()
    select_currency_rate_query = "SELECT rate " \
                                 "FROM currency " \
                                 "WHERE code = 'EUR'"  #because there is no currency parameter in query
    cursor.execute(select_currency_rate_query)
    rate_cortage = cursor.fetchall()
    third_rebill_row = rate_cortage[0]
    return third_rebill_row[0]


"""Calculate third rebill money_from_gateway using currency rate"""
def calculate_third_rebill_money_from_gateway_using_currency():
    calculate_payout = select_third_rebill_currency_rate() \
                       * float(case_1_third_rebill_params['payout'])
    return calculate_payout

"""Define third rebill user base coefficient"""
def select_third_rebill_user_base_coefficient():
    cursor = connection.cursor()
    select_user_base_coefficient = "SELECT base_coefficient " \
                                   "FROM \"user\" " \
                                   "WHERE id = {}".format(save_third_rebill[3])
    cursor.execute(select_user_base_coefficient)
    base_coefficient_cortage = cursor.fetchall()
    base_coefficient = base_coefficient_cortage[0]
    return base_coefficient[0]


"""Validate third rebill money_from_gateway"""
if calculate_third_rebill_money_from_gateway_using_currency() == \
        float(case_1_third_rebill_params['payout']) * select_third_rebill_currency_rate():
    print('third rebill money_from_gateway true')
else:
    print('third rebill money_from_gateway false')


"""Validate third rebill money_for partner"""
if round(float(select_third_rebill_user_base_coefficient()
               * calculate_third_rebill_money_from_gateway_using_currency()),2) \
        == round(float(save_third_rebill[5]),2):
    print("third rebill money_for partner true")
else:
    print("third rebill money_for partner false")


"""Validate third is_payout_received"""
def select_third_rebill_is_payout_received():
    cursor = connection.cursor()
    select_is_payout_received = "SELECT is_payout_received " \
                                "FROM rebill " \
                                "WHERE click_id = {} " \
                                "AND external_message_id = '{}'".format(used_click_for_subscription,
                                                                        case_1_third_rebill_params[
                                                                            'text_uniq_lead'])
    cursor.execute(select_is_payout_received)
    is_payout_received_cortage = cursor.fetchall()
    is_payout_received = is_payout_received_cortage[0]
    return is_payout_received[0]


def third_rebill_check_key_value():
    is_payout = 'payout' in case_1_third_rebill_params
    return is_payout


if select_third_rebill_is_payout_received() == third_rebill_check_key_value():
    print("third rebill is_payout_received = true. Test was passed")
else:
    print("third rebill is_payout_received = false. test wasn't passed")


"""Validate third_rebill extra_param"""
if save_third_rebill[17] == case_1_third_rebill_params['extra_param']:
    print('third rebill extra_param true')
else:
    print('third rebill extra_param false')


"""Validate third rebill user role"""
def select_third_rebill_user_role():
    cursor = connection.cursor()
    select_user_role = "SELECT role " \
                       "FROM \"user\" " \
                       "WHERE id = {}".format(save_third_rebill[3])
    cursor.execute(select_user_role)
    user_role_cortage = cursor.fetchall()
    user_role = user_role_cortage[0]
    return user_role[0]

if select_third_rebill_user_role() == save_third_rebill[18]:
    print('third rebill user_role true')
else:
    print('third rebill user_role false')


"""
========================================================================================
========================================================================================
From this place we start validate fourth created rebill
"""


def select_created_fourth_rebill():
    cursor = connection.cursor()
    fourth_rebill_select_query = "SELECT * " \
                                "FROM rebill " \
                                "WHERE click_id = {} AND external_message_id = '{}'".format(used_click_for_subscription,
                                                                                            case_1_fourth_rebill_params[
                                                                                                'text_uniq_lead'])
    cursor.execute(fourth_rebill_select_query)
    fourth_rebill_cortage = cursor.fetchall()
    fourth_rebill_row = fourth_rebill_cortage[0]
    return fourth_rebill_row


"""Save selected fourth rebill data into variable"""
save_fourth_rebill = select_created_fourth_rebill()


"""Select fourth rebill click_id and validate it"""
def fourth_rebill_click_id():
    fourth_rebill_click_id = save_fourth_rebill[6]
    return str(fourth_rebill_click_id)

if case_1_fourth_rebill_params['click_id'] == fourth_rebill_click_id():
    print('fourth_rebill_click_id true')
else:
    print('fourth_rebill_click_id false')



"""Select fourth rebill gateway_id for validation after"""
def define_fourth_rebill_gateway_id():
    cursor = connection.cursor()
    gateway_select_query = "SELECT * " \
                           "FROM gateway_aliases " \
                           "WHERE alias = '{}'".format(case_1_fourth_rebill_params['partner'])
    cursor.execute(gateway_select_query)
    gateway_cortage = cursor.fetchall()
    gateway_parameters = gateway_cortage[0]
    gateway_id = gateway_parameters[2]
    return str(gateway_id)

def fourth_rebill_gateway_id():
    return str(save_fourth_rebill[2])

if define_fourth_rebill_gateway_id() == fourth_rebill_gateway_id():
    print('fourth_rebill_gateway_id true')
else:
    print('fourth_rebill_gateway_id false')


"""Validate fourth_rebill external_message_id(text_uniq_lead)"""
if case_1_fourth_rebill_params['text_uniq_lead'] == save_fourth_rebill[10]:
    print('fourth_rebill_external_message_id true')
else:
    print('fourth_rebill_external_message_id false')


"""Validate fourth rebill external_subscription_id"""
if case_1_fourth_rebill_params['subscr'] == save_subscription_parameters[2]:
    print('fourth rebill external_subscription_id true')
else:
    print('fourth rebill external_subscription_id false')


"""Validate related with fourth rebill's money parameters"""
def select_fourth_rebill_sms_offer_payout():
    cursor = connection.cursor()
    select_fourth_rebill_sms_offer_payout = "SELECT payout " \
                                            "FROM sms_offer " \
                                            "WHERE id = {}".format(save_fourth_rebill[9])
    cursor.execute(select_fourth_rebill_sms_offer_payout)
    fourth_rebill_sms_offer_payout_cortage = cursor.fetchall()
    fourth_rebill_sms_offer_payout = fourth_rebill_sms_offer_payout_cortage[0]
    return fourth_rebill_sms_offer_payout[0]


"""Define fourth rebill user base coefficient"""
def select_fourth_rebill_user_base_coefficient():
    cursor = connection.cursor()
    select_user_base_coefficient = "SELECT base_coefficient " \
                                   "FROM \"user\" " \
                                   "WHERE id = {}".format(save_fourth_rebill[3])
    cursor.execute(select_user_base_coefficient)
    base_coefficient_cortage = cursor.fetchall()
    base_coefficient = base_coefficient_cortage[0]
    return base_coefficient[0]

"""Calculate fourth rebill money_from_gateway"""
def calculate_fourth_rebill_money_from_gateway():
    calculate_payout = float(select_fourth_rebill_sms_offer_payout()) \
                       * float(select_fourth_rebill_user_base_coefficient())
    return calculate_payout


"""Validate fourth rebill money_from_gateway"""
if select_fourth_rebill_sms_offer_payout() == save_fourth_rebill[4]:
    print("fourth rebill money_from_gateway true")
else:
    print("fourth rebill money_from_gateway false")


"""Validate fourth rebill money_for_partner"""
if save_fourth_rebill[5] == calculate_fourth_rebill_money_from_gateway():
    print("fourth rebill money_for_partner true")
else:
    print("fourth rebill money_for_partner false")


def fourth_rebill_check_key_value():
    is_payout = 'payout' in case_1_fourth_rebill_params
    return is_payout


if save_fourth_rebill[16] == fourth_rebill_check_key_value():
    print('Fourth rebill is_payout_received = false. Test was passed')
else:
    print("Fourth rebill is_payout_received = true. Test wasn't passed")



"""Validate fourth_rebill extra_param"""
if save_fourth_rebill[17] == case_1_fourth_rebill_params['extra_param']:
    print('fourth rebill extra_param true')
else:
    print('fourth rebill extra_param false')


"""Validate fourth rebill user role"""
def select_fourth_rebill_user_role():
    cursor = connection.cursor()
    select_user_role = "SELECT role " \
                       "FROM \"user\" " \
                       "WHERE id = {}".format(save_fourth_rebill[3])
    cursor.execute(select_user_role)
    user_role_cortage = cursor.fetchall()
    user_role = user_role_cortage[0]
    return user_role[0]


if select_fourth_rebill_user_role() == save_fourth_rebill[18]:
    print('fourth rebill user_role true')
else:
    print('fourth rebill user_role false')
