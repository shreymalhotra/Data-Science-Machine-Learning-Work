
test = {
  'name': 'q03c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> expected = [('DEM', 58), (None, 44), ('REP', 8), ('UNK', 4), ('NNE', 2), ('GRE', 1)]
>>> connection.execute(query_q3c).fetchall() == expected
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
