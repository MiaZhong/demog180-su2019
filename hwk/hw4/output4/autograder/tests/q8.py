test = {   'name': 'q8',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "round(float(np.mean(add_health_sp.column('num_nodes'))), "
                                               '2)\n'
                                               '860.26',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "round(float(np.corrcoef(add_health_sp.column('avg_shortest_path'),add_health_sp.column('avg_degree'))[0,1]),2)\n"
                                               '-0.65',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
