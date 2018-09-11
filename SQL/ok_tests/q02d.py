
test = {
  'name': 'q02d',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> func = lambda x:list(map(lambda y:(y[0],int(y[1]),y[2]),x))
>>> expected = [('ATTORNEY', 423, 56), ('SOFTWARE ENGINEER', 371, 13), ('CONSULTANT', 343, 12), ('STUDENT', 317, 11), ('SCIENTIST', 298, 30), ('ENGINEER', 228, 20), ('ARTIST', 216, 19), ('PHYSICIAN', 193, 18), ('RETIRED', 143, 306), ('UNEMPLOYED', 140, 18)]
>>> func(connection.execute(query_q2d).fetchall()) == expected
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
