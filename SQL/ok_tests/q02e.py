
test = {
  'name': 'q02e',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> func = lambda x:list(map(lambda y:(y[0],y[1],int(y[2])),x))
>>> expected = [('LOUISE GUND FOUNDATION', 'GUND, LOUISE LAIDLAW', 25000), ('INVESTOR/BOARD MEMBER', 'FIDDLER, JERRY', 10000), ('SCIENTIST', 'SHENKER, SCOTT', 8000), ('RETIRED', 'BERLEKAMP, ELWYN', 5550), ('ATTORNEY', 'ABRAMS, DENISE', 5400), ('NOT EMPLOYED', 'LUEVANO, ROSA', 5000), ('MARRIAGE & FAMILY THERAPIST', 'LAPPEN, DAVID', 5000), ('SOFTWARE ENGINEER', 'HUFF, GERALD', 3200), ('RETIRED', 'BERNHARDT, ANTHONY', 3200), ('MANAGER', 'SEIBEL, PETER', 2700)]
>>> func(connection.execute(query_q2e).fetchall())[:5] == expected[:5]
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
