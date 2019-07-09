test = {   'name': 'q12',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'round(np.mean(er_res.column(0)), '
                                               '2)\n'
                                               '0.029999999999999999',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'round(np.mean(er_res.column(1)), '
                                               '2)\n'
                                               '2.8799999999999999',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "round(np.corrcoef(er_res['cc'], "
                                               "er_res['apl'])[0,1],2)\n"
                                               '-0.029999999999999999',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
