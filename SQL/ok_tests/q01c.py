
test = {
  'name': 'q01c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> expected = [('GUND, LOUISE LAIDLAW', 25000), ('FIDDLER, JERRY', 10000), ('SHENKER, SCOTT', 8000), ('BERLEKAMP, ELWYN', 5550), ('ABRAMS, DENISE', 5400), ('LAPPEN, DAVID', 5000), ('LUEVANO, ROSA', 5000), ('BERNHARDT, ANTHONY', 3200), ('HUFF, GERALD', 3200), ('BIRD, KAREN', 2700), ('EPSTEIN, BOB', 2700), ('HAHN, SOPHIE', 2700), ('JOSEPH, DAVID', 2700), ('LITTMANN, NICOLE', 2700), ('LOGAN, JONATHAN', 2700), ('REINIS, JONATHAN ROY', 2700), ('SEIBEL, PETER', 2700), ('SHAPIRO, CARL', 2700), ('TAYLOR, JEROME', 2700), ('WILNER, DAVID', 2700)]
>>> connection.execute(query_q1c).fetchall() == expected
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
