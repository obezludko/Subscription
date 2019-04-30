from click_sub.click_with_user_coefficient import get_click_id_from_responce


"""Case presents valid parameters for creating subscription"""
used_click_for_subscription = get_click_id_from_responce()

case_4_first_subscription_params = {'partner': 'test',
                                    'action': 'init',
                                    'click_id': used_click_for_subscription,
                                    'external_message_id': used_click_for_subscription + 'q1',
                                    'external_subscription_id': used_click_for_subscription + 'w1',
                                    'extra_param': 'case 4 SUB'
                                    }


case_4_second_subscription_params = {'partner': 'test',
                                    'action': 'init',
                                    'click_id': used_click_for_subscription,
                                    'external_message_id': used_click_for_subscription + 'q40',
                                    'external_subscription_id': used_click_for_subscription + 'w2',
                                    'extra_param': 'case 4 SUB'
                                    }