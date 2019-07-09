test = {   'name': 'q5',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'add_health_clustering.num_rows\n'
                                               '84',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "round(float(np.corrcoef(add_health_clustering.column('num_nodes'), "
                                               "add_health_clustering.column('avg_clustering_coef'))[0,1]), "
                                               '2)\n'
                                               '-0.66',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
