test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
    'type':'wwpp',
      'cases': [
        {
          'code': """
          >>> sim_results_aggregate.column('num_infected_degree mean').mean()<sim_results_aggregate.column('num_infected_ec mean').mean()
          True
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
