test = {   'name': 'q6',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'round(party_degree.where("party","Democrat").column(\'degree '
                                               "mean')[0],0)\n"
                                               '175.0',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'round(party_degree.where("party","Independent").column(\'degree '
                                               "mean')[0],3)\n"
                                               '145.5',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'round(party_degree.where("party","Republican").column(\'degree '
                                               "mean')[0],3)\n"
                                               '191.113',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
