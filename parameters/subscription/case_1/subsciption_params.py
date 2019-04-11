from click_sub.click import parse_url_and_append_click

"""Case present not only required parameters for creating subscription"""

used_click_for_subscription = parse_url_and_append_click()

case_1_subscription_params = {'partner': 'test',
                              'action': 'SUBSCRIBE',                             # one of 3 action subscribe action(subscribe,SUBSCRIBE, init)
                              'click_id': used_click_for_subscription,
                              'external_message_id': used_click_for_subscription + 'q1',
                              'external_subscription_id': used_click_for_subscription + 'w1',
                              'currency': 'ALL',                                  # 1 All = 5 EUR
                              'payout': '1',
                              'extra_param': 'subTEST123'}

# print(external_message_id, '\n', external_subscription_id)
