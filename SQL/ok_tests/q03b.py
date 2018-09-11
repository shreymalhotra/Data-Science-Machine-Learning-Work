
test = {
  'name': 'q03b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> expected = [('ACTBLUE', None, 'SOMERVILLE', 'MA', 66228, 799), ('HILLARY FOR AMERICA', 'DEM', 'NEW YORK', 'NY', 38002, 252), ('BERNIE 2016', 'DEM', 'BURLINGTON', 'VT', 19920, 239), ('DCCC', 'DEM', 'WASHINGTON', 'DC', 26040, 153), ('DSCC', 'DEM', 'WASHINGTON', 'DC', 7271, 71), ('END CITIZENS UNITED', None, 'WASHINGTON', 'DC', 1129, 47), ('HILLARY VICTORY FUND', None, 'NEW YORK', 'NY', 44163, 45), ('MOVEON.ORG POLITICAL ACTION', None, 'WASHINGTON', 'DC', 2836, 37), ('CATHERINE CORTEZ MASTO FOR SENATE', 'DEM', 'LAS VEGAS', 'NV', 6878, 27), ("EMILY'S LIST", None, 'WASHINGTON', 'DC', 7988, 26)]
>>> connection.execute(query_q3b).fetchall() == expected
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
