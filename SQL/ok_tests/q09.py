
test = {
  'name': 'q09',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> r=connection.execute("SET SEED TO " + str(seed))
>>> res = connection.execute(query_q9).fetchall()
>>> # If you fail this test, you aren't computing the right number of rows in your query
>>> len(res) == 2000
True
>>> 
>>> trials.shape == (1000, 1)
True
>>> # Check that there is some variation in the trials
>>> np.std(trials['stats']) != 0
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
