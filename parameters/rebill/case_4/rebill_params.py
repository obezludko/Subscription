from parameters.subscription.case_4.subscription_params import used_click_for_subscription

case_4_first_rebill_params = {'partner': 'test',
                              'action': 'rebill',
                              'click_id': used_click_for_subscription,
                              'external_message_id': used_click_for_subscription + 'q2',
                              'external_subscription_id': used_click_for_subscription + 'w1',
                              'extra_param': 'EXtra reb_1'
                              }

case_4_second_rebill_params = {'partner': 'test',
                              'action': 'rebill',
                              'click_id': used_click_for_subscription,
                              'external_message_id': used_click_for_subscription + 'q3',
                              'external_subscription_id': used_click_for_subscription + 'w1',
                              'extra_param': 'EXtra reb_2'
                              }