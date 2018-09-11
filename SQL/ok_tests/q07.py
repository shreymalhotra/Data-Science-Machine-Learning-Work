test = {
  'name': 'q07',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> r=connection.execute("drop view if exists design cascade")
>>> r=connection.execute("SET SEED TO " + str(seed))
>>> r=connection.execute(query_q7)
>>> # Test that your view has the right length
>>> connection.execute("select count(*) from design").fetchall() == [(491000,)]
True
>>> # If you fail these tests, you aren't shuffling the rows within each group only
>>> connection.execute("select SUM(row_id) from design where trial_id = 1").fetchall() == [(120786,)]
True
>>> connection.execute("select SUM(row_id) from design where trial_id = 2").fetchall() == [(120786,)]
True
>>> connection.execute("select SUM(row_id) from design where trial_id = 3").fetchall() == [(120786,)]
True
>>> connection.close()
>>> connection = engine.connect()
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