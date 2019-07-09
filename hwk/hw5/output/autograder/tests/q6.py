test = {   'name': 'q6',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "np.round(np.mean(nbr_avg_degrees['avg_friends_degree']), "
                                               '2)\n'
                                               '7.71',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "round(nbr_avg_degrees.where(nbr_avg_degrees['id'] "
                                               '== '
                                               "6)['avg_friends_degree'][0], "
                                               '2) == 5.4\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
