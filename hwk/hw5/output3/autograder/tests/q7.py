test = {   'name': 'q7',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "round(float(np.mean(friend_data['degree'])), "
                                               '2)\n'
                                               '6.38',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "round(friend_data.where(friend_data['id'] "
                                               "== 6)['degree'][0], 2) == 5\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
