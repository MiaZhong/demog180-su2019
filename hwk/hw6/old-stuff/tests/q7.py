test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type':'wwpp',
      'cases': [
        {
          'code': """
          >>> (round(gender_degree.where("gender","F").column('degree mean')[0],3)==197.286) and (round(gender_degree.where("gender","M").column('degree mean')[0],3)==180.679) 
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
