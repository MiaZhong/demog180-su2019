test = {   'name': 'q12',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'round(float(np.mean(er_res.column(0))), '
                                               '2)\n'
                                               '0.03',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'round(float(np.mean(er_res.column(1))), '
                                               '2)\n'
                                               '2.89',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "round(float(np.corrcoef(er_res['cc'], "
                                               "er_res['apl'])[0,1]),2)\n"
                                               '-0.25',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
