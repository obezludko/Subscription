from parameters.subscription.case_3.subscription_params import used_click_for_subscription


case_3_first_rebill_params = {'partner': 'test',
                              'action': 'rebill',
                              'click_id': used_click_for_subscription,
                              'external_message_id': used_click_for_subscription + 'q2',
                              'external_subscription_id': used_click_for_subscription + 'w1',
                              'currency': 'ALL',
                              'payout': '1,5',  # Payout must be a number
                              'extra_param': 'REBill 1'
                              }

case_3_second_rebill_params = {'partner': 'test',
                               'action': 'rebill',
                               'click_id': used_click_for_subscription,
                               'external_message_id': used_click_for_subscription + 'q3',
                               'external_subscription_id': used_click_for_subscription + 'w1',
                               'currency': 'all',  # Writed in lowercase currency hasn't pass
                               'payout': '1',
                               'extra_param': 'REBill 2'
                               }

case_3_third_rebill_params = {'partner': 'test',
                              'action': 'rebill',
                              'click_id': used_click_for_subscription,
                              'text_uniq_lead': used_click_for_subscription + 'q1',  # not unique external_message_id
                              'subscr': used_click_for_subscription + 'w1',
                              'extra_param': 'REBill 3'
                              }

case_3_fourth_rebill_params = {'partner': 'test',
                               'action': 'rebill',
                               'click_id': used_click_for_subscription,
                               'text_uniq_lead': used_click_for_subscription + 'q4',
                               'subscr': used_click_for_subscription + 'w1111',
                               # external_subscription_id doesn't exist
                               'extra_param': 'REBill 4'
                               }

case_3_fifth_rebill_params = {'partner': 'Alalo666',  # Partner doesn't exist
                              'action': 'BILLING',
                              'click_id': used_click_for_subscription,
                              'external_message_id': used_click_for_subscription + 'q5',
                              'subscr': used_click_for_subscription + 'w1',
                              'extra_param': 'REBill 5'
                              }

case_3_sixth_rebill_params = {'action': 'BILLING',  # Without partner parameter
                              'click_id': used_click_for_subscription,
                              'external_message_id': used_click_for_subscription + 'q6',
                              'subscr': used_click_for_subscription + 'w1',
                              'extra_param': 'REBill 6'
                              }

case_3_seventh_rebill_params = {'partner': 'test',
                                'action': 'UNKNOWN',  # UNKNOWN action
                                'click_id': used_click_for_subscription,
                                'external_message_id': used_click_for_subscription + 'q7',
                                'subscr': used_click_for_subscription + 'w1',
                                'extra_param': 'REBill 7'
                                }

case_3_eighth_rebill_params = {'partner': 'test',  # without action
                               'click_id': used_click_for_subscription,
                               'external_message_id': used_click_for_subscription + 'q8',
                               'subscr': used_click_for_subscription + 'w1',
                               'extra_param': 'REBill 8'
                               }

case_3_ninth_rebill_params = {'partner': 'test',
                              'action': 'REBILL',
                              'click_id': '',  # without click_id
                              'external_message_id': used_click_for_subscription + 'q9',
                              'subscr': used_click_for_subscription + 'w1',
                              'extra_param': 'REBill 9'
                              }
