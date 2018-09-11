test = {
  'name': 'Question 1a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(bike, pd.DataFrame)
          True
          >>> bike.shape == (17379, 17) or bike.shape == (17379, 18)
          True
          >>> bike['holiday'].dtype == np.dtype('O')
          True
          >>> list(bike['holiday'].iloc[370:375]) == ['no', 'no', 'yes', 'yes', 'yes']
          True
          >>> 400 <= num_holidays <= 550
          True
          >>> num_holidays == 500
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
