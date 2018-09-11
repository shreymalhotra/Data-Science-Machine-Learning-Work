
test = {
  'name': 'q02f',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> func = lambda x:list(map(lambda y:(y[0],int(y[1]),y[2]),x))
>>> expected = [('SCIENTIST', 1118, 8), ('ATTORNEY', 593, 40), ('SOFTWARE ENGINEER', 535, 9), ('CONSULTANT', 374, 11), ('STUDENT', 349, 10), ('NOT-EMPLOYED', 331, 9), ('ARTIST', 273, 15), ('PHYSICIAN', 268, 13), ('ENGINEER', 253, 18), ('PROFESSOR', 240, 32)]
>>> func(connection.execute(query_q2f).fetchall()) == expected
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
