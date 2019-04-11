from parameters.subscription.case_1.subsciption_params import used_click_for_subscription

"""parameters for"""

case_1_cancel_params = {'partner': 'test',
                        'action': 'UNSUBSCRIBE',  # one of 2 cancel actions(cancel,UNSUBSCRIBE)
                        'click_id': used_click_for_subscription,
                        'text_uniq_lead': used_click_for_subscription + 'q6',
                        'subscr': used_click_for_subscription + 'w1',
                        'extra_param': 'cancel_1'}
