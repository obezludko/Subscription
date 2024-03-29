from click_sub.click import parse_url_and_append_click

"""Case presents not valid parameters for creating subscription. 
After test running subscriptions won't be created"""

used_click_for_subscription = parse_url_and_append_click()

case_2_first_subscription_params = {'partner': 'test',
                                    'action': 'init',  # one of 3 action subscribe action(subscribe,SUBSCRIBE, init)
                                    'click_id': used_click_for_subscription,
                                    'external_message_id': used_click_for_subscription + 'q1',  # text_uniq_lead || external_message_id
                                    'external_subscription_id': used_click_for_subscription + 'w1',  # external_subscription_id || subscr
                                    'currency': 'usd',  # writed in lowercase currency hasn't pass
                                    'extra_param': 'subTWO123'}


case_2_second_subscription_params = {'partner': 'test',
                                     'action': 'SUBSCRIBE',
                                     'click_id': '',  # click id field is required
                                     'external_message_id': used_click_for_subscription + 'q2',
                                     'external_subscription_id': used_click_for_subscription + 'w2'}


case_2_third_subscription_params = {'partner': 'test',
                                    'action': 'UNKNOWN',  # UNKNOWN action
                                    'click_id': used_click_for_subscription,
                                    'external_message_id': used_click_for_subscription + 'q3',
                                    'external_subscription_id': used_click_for_subscription + 'w3'}


case_2_fourth_subscription_params = {'partner': 'eboy',
                                     'action': 'subscribe',
                                     'click_id': used_click_for_subscription,
                                     'text_uniq_lead': used_click_for_subscription + 'q4',
                                     'subscr': used_click_for_subscription + 'w4',
                                     'payout': '0,1'  # Payout must be a number.
                                     }


case_2_fifth_subscription_params = {'partner': 'alavala666',  # partner don't exist
                                    'action': 'init',
                                    'click_id': used_click_for_subscription,
                                    'external_message_id': used_click_for_subscription + 'q5',
                                    'subscr': used_click_for_subscription + 'w5'
                                    }


case_2_sixth_subscription_params = {'partner': '',  # blank partner parameter
                                    'action': 'init',
                                    'click_id': used_click_for_subscription,
                                    'external_message_id': used_click_for_subscription + 'q6',
                                    'subscr': used_click_for_subscription + 'w6'
                                    }


case_2_seventh_subscription_params = {'partner': 'test',
                                      'action': 'subscribe',
                                      'click_id': used_click_for_subscription,
                                      'external_message_id': used_click_for_subscription + 'q7',
                                      'external_subscription_id': used_click_for_subscription + 'w7',
                                      'extra_param': '12345678901234567890123456'  # 26 symbols (parameter expects !>25)
                                      }
