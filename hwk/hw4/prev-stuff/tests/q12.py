test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.mean(er_res.column(0)) > 0.027
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.mean(er_res.column(1)) > 2
          True
          """,
          'hidden': False,
          'locked': False
        }                
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}