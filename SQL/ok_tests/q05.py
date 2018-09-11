
test = {
  'name': 'q05',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> expected = [('HAHN, SOPHIE', 2700, 'HILLARY FOR AMERICA'), ('JOSEPH, DAVID', 2700, 'HILLARY FOR AMERICA'), ('LITTMANN, NICOLE', 2700, 'BERNIE 2016'), ('LOGAN, JONATHAN', 2700, 'BERNIE 2016'), ('REINIS, JONATHAN ROY', 2700, 'HILLARY FOR AMERICA')]
>>> r=connection.execute("DROP VIEW IF EXISTS contribs CASCADE")
>>> r=connection.execute(query_q5)
>>> connection.execute("SELECT * FROM contribs LIMIT 5").fetchall() == expected
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
