
test = {
  'name': 'q01a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> connection.execute(query_q1a).fetchall() == [(4,)]
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
