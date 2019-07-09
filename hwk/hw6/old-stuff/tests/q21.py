test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
    'type':'wwpp',
      'cases': [
        {
          'code': """
          >>> ((moc_target_bc_mean_infected-3)<1) or ((moc_target_bc_mean_infected-1)<1)
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
