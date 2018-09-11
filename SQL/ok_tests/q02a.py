
test = {
  'name': 'q02a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> connection.execute(query_q2a).fetchall() == [(407,)]
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
