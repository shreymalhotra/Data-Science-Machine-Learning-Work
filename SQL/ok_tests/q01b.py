
test = {
  'name': 'q01b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> expected = [('C00586537', 'GUND, LOUISE LAIDLAW', 25000), ('C00000935', 'FIDDLER, JERRY', 10000), ('C00586537', 'LAPPEN, DAVID', 5000), ('C00401224', 'LUEVANO, ROSA', 5000)]
>>> connection.execute(query_q1b).fetchall() == expected
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
