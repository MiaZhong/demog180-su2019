test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type':'wwpp',
      'cases': [
        {
          'code': """
          >>> (round(party_degree.where("party","Democrat").column('degree mean')[0],3)==175.27) and (round(party_degree.where("party","Independent").column('degree mean')[0],3)==145.5) and (round(party_degree.where("party","Republican").column('degree mean')[0],3)==191.113)
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
