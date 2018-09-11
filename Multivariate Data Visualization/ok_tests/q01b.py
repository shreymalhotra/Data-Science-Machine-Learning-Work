test = {
  'name': 'Question 1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> bike['weekday'].dtype == np.dtype('O')
          True
          >>> bike['workingday'].dtype == np.dtype('O')
          True
          >>> bike['weathersit'].dtype == np.dtype('O')
          True
          >>> list(bike['weekday'].iloc[::2000]) == ['Sat', 'Tue', 'Mon', 'Mon', 'Mon', 'Sun', 'Sun', 'Sat', 'Sun']
          True
          >>> list(bike['workingday'].iloc[::2000]) == ['no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'no']
          True
          >>> list(bike['weathersit'].iloc[::2000]) == ['Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Clear']
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
