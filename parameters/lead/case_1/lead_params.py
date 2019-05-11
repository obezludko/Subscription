from click_sub.click import parse_url_and_append_click

"""Case present only required parameters.
 Lead hasn't be created"""

used_click_for_lead = parse_url_and_append_click()

case_1_first_lead_params = {'partner': '',
                            'click_id': used_click_for_lead,
                            'external_message_id': '',
                            'payout': '0.1'}

case_1_second_lead_params = {'partner': '',
                             'click_id': used_click_for_lead,
                             'text_uniq_lead': '',
                             'currency': 'USD'}

case_1_third_lead_params = {'partner': 'INVALID_666',
                            'click_id': used_click_for_lead,
                            'external_message_id': ''}

case_1_fourth_lead_params = {'partner': '',
                             'click_id': used_click_for_lead,
                             'text_uniq_lead': ''}

case_1_fifth_lead_params = {'partner': '',
                            'click_id': used_click_for_lead + 'abc',
                            'external_message_id': ''}

case_1_sixth_lead_params = {'partner': '',
                            'click_id': used_click_for_lead,
                            'text_uniq_lead': used_click_for_lead + 'Q1'}

case_1_seventh_lead_params = {'partner': 'test',
                              'click_id': used_click_for_lead,
                              'text_uniq_lead': ''}

case_1_eighth_lead_params = {'partner': 'test',
                             'click_id': '',
                             'text_uniq_lead': used_click_for_lead + 'Q2'}

case_1_ninth_lead_params = {'click_id': used_click_for_lead,
                            'text_uniq_lead': used_click_for_lead + 'Q3'}

case_1_tenth_lead_params = {'partner': 'test',
                            'text_uniq_lead': used_click_for_lead + 'Q4'}

case_1_eleventh_lead_params = {'partner': 'test',
                               'click_id': used_click_for_lead}


case_1_twelfth_lead_params = {'partner': 'test',
                              'click_id': used_click_for_lead,
                              'external_message_id': used_click_for_lead + 'Q5',
                              'currency': 'usd'}  # expects uppercase value

case_1_thirteenth_lead_params = {'partner': 'test',
                                 'click_id': used_click_for_lead,
                                 'external_message_id': used_click_for_lead + 'Q6',
                                 'payout': '1,1'}  # expects type float

case_1_fourteenth_lead_params = {'partner': 'test',
                                 'click_id': used_click_for_lead,
                                 'external_message_id': used_click_for_lead + 'Q7',
                                 'payout': 'abc'} # expects type float

case_1_fifteenth_lead_params = {'partner': 'TEST', # we haven't this partner alias
                                'click_id': used_click_for_lead,
                                'external_message_id': used_click_for_lead + 'Q8'}
