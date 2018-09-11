
test = {
  'name': 'q03a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> expected = [('C00401224', 66228, 799), ('C00575795', 38002, 252), ('C00577130', 19920, 239), ('C00000935', 26040, 153), ('C00042366', 7271, 71)]
>>> connection.execute(query_q3a).fetchall() == expected
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
