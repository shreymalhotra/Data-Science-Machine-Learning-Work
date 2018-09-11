
test = {
  'name': 'q02a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> len(exact_bootstrap) == 7**7
True
>>> min(exact_bootstrap) == -12
True
>>> max(exact_bootstrap) == 18
True
>>> sum(exact_bootstrap == 0) == 10368
True
>>> sum(exact_bootstrap == 6) == 25075
True
>>> sum(exact_bootstrap == 8) == 17598
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
