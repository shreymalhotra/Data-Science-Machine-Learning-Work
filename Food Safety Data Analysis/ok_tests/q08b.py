test = {
  'name': 'Question 8b',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(vio2016) == 16961
          True
          >>> all(vio2016['year'] == 2016)
          True
          >>> all(isinstance(d,pd.datetime) for d in vio['new_date'])
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
