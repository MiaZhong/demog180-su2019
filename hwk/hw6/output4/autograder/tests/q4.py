test = {   'name': 'q4',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'moc_node_centrality_dat.num_rows\n'
                                               '519',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "round(moc_node_centrality_dat.column('betweenness_centrality').mean(),5)\n"
                                               '0.00125',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "round(moc_node_centrality_dat.column('eigenvector_centrality').mean(),5)\n"
                                               '0.04088',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "round(moc_node_centrality_dat.column('degree').mean(),1)\n"
                                               '184.0',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
