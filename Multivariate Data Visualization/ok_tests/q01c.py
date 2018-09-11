test = {
  'name': 'Question 1c',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.round(daily_counts['casual'].mean())
          848.0
          >>> np.round(daily_counts['casual'].var())
          471450.0
          >>> np.round(daily_counts['registered'].mean())
          3656.0
          >>> np.round(daily_counts['registered'].var())
          2434400.0
          >>> sorted(list(daily_counts['workingday'].value_counts()))
          [231, 500]
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
