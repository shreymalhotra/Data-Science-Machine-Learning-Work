
test = {
  'name': 'q02c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> func = lambda x:list(map(lambda y:(y[0],int(y[1]),y[2]),x))
>>> expected = [('LOUISE GUND FOUNDATION', 25000, 1), ('INVESTOR/BOARD MEMBER', 10000, 1), ('MARRIAGE & FAMILY THERAPIST', 5000, 1), ('INVESTMENT MANAGEMENT', 2700, 1), ('LIVE THEATRE PRODUCER', 2700, 1), ('CHAIRMAN', 2700, 1), ('AIDS CASE MANAGER', 2500, 1), ('WEALTH MANAGER', 1700, 1), ('INVESTOR', 1485, 2), ('ACCOUNTANT', 1475, 2)]
>>> func(connection.execute(query_q2c).fetchall())[:3] == expected[:3]
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
