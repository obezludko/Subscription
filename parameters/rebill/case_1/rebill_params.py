from parameters.subscription.case_1.subsciption_params import used_click_for_subscription

"""Case present not only required parameters for creating rebill for created subscription.
    We use different aliases for parameters and differend aliases for actions."""

"""With payout and currency"""

case_1_first_rebill_params = {'partner': 'test',
                              'action': 'BILLING',  # one of 2 rebill actions(rebill,BILLING)
                              'click_id': used_click_for_subscription,
                              'external_message_id': used_click_for_subscription + 'q2',
                              'external_subscription_id': used_click_for_subscription + 'w1',
                              'currency': 'ALL',
                              'payout': '1',  # 1 All = 5 EUR
                              'extra_param': 'rebill_1'}

"""With payout and another currency"""

case_1_second_rebill_params = {'partner': 'test',
                               'action': 'rebill',  # one of 2 rebill actions(rebill,BILLING)
                               'click_id': used_click_for_subscription,
                               'text_uniq_lead': used_click_for_subscription + 'q3',
                               'subscr': used_click_for_subscription + 'w1',
                               'currency': 'EUR',
                               'payout': '1.5',  # 1 EUR = 1 EUR
                               'extra_param': 'rebill_2'}

"""With payout and without currency"""

case_1_third_rebill_params = {'partner': 'test',
                              'action': 'BILLING',  # one of 2 rebill actions(rebill,BILLING)
                              'click_id': used_click_for_subscription,
                              'text_uniq_lead': used_click_for_subscription + 'q4',
                              'subscr': used_click_for_subscription + 'w1',
                              'payout': '1',  # 1 EUR = 1 EUR
                              'extra_param': 'rebill_3'}

"""Without payout and currency"""

case_1_fourth_rebill_params = {'partner': 'test',
                               'action': 'BILLING',  # one of 2 rebill actions(rebill,BILLING)
                               'click_id': used_click_for_subscription,
                               'text_uniq_lead': used_click_for_subscription + 'q5',
                               'subscr': used_click_for_subscription + 'w1',
                               'extra_param': 'rebill_4'}
