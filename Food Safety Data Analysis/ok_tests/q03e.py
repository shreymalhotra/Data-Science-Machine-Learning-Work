test = {
  'name': 'Question 3e',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(bus[bus['zip_code'] == "94602"]) == 0
          True
          >>> len(bus[bus['zip_code'] == "94102"]) == 459
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
