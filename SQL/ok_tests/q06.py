
test = {
  'name': 'q06',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> expected = [('BERNIE 2016', 212, 239), ('HILLARY FOR AMERICA', 225, 252)]
>>> connection.execute(query_q6).fetchall() == expected
True
>>> np.allclose(observed_stat, 0.0058278541542140516)
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
