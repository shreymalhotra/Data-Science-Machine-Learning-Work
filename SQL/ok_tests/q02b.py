
test = {
  'name': 'q02b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> expected = [('NOT EMPLOYED', 373), ('RETIRED', 306), (None, 70), ('PROFESSOR', 58), ('ATTORNEY', 56), ('NONE', 33), ('SCIENTIST', 30), ('RETIRED TEACHER', 20), ('ENGINEER', 20), ('PHONE CLERK', 20), ('ARTIST', 19), ('PSYCHOLOGIST', 19), ('HOMEMAKER', 19), ('UNEMPLOYED', 18), ('WRITER', 18), ('PHYSICIAN', 18), ('TEACHER', 17), ('LAWYER', 16), ('PSYCHOTHERAPIST', 16), ('PROFESSIONAL', 15)]
>>> connection.execute(query_q2b).fetchall()[:6] == expected[:6]
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
