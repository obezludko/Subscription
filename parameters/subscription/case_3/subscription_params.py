from click_sub.click import parse_url_and_append_click

"""Case presents valid parameters for creating subscription"""

used_click_for_subscription = parse_url_and_append_click()

case_3_first_subscription_params = {'partner':'test',
                                    'action':'init',
                                    'click_id': used_click_for_subscription,
                                    'external_message_id': used_click_for_subscription + 'q1',
                                    'external_subscription_id': used_click_for_subscription + 'w1',
                                    'currency':'ALL',
                                    'pauout':'1.5',
                                    'extra_param':'case 3 SUB'
                                    }

case_3_first_rebill_params = {}