test = {   'name': 'q12',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "str(round(np.mean(add_health_msmts['avg_degree']), "
                                               '5))\n'
                                               "'7.23103'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "str(round(np.mean(add_health_msmts['avg_neighbor_degree']), "
                                               '5))\n'
                                               "'8.79592'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "str(round(np.mean(add_health_msmts['frac_lt_neighbors']), "
                                               '5))\n'
                                               "'0.68504'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "str(round(np.corrcoef(add_health_msmts['avg_degree'], "
                                               "add_health_msmts['avg_neighbor_degree'])[0,1], "
                                               '5))\n'
                                               "'0.98939'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "str(round(np.corrcoef(add_health_msmts['avg_neighbor_degree'], "
                                               "add_health_msmts['frac_lt_neighbors'])[0,1], "
                                               '5))\n'
                                               "'0.03092'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
