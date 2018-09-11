
test = {
  'name': 'q08',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> r=connection.execute(q_sample)
>>> r=connection.execute("drop view if exists joined cascade")
>>> r=connection.execute("SET SEED TO " + str(seed))
>>> r=connection.execute(query_q8)
>>> # If you fail this test, you're shuffling the committee names along with the transaction amounts
>>> q1 = "select sum(transaction_amt) from joined where trial_id = 1 group by cmte_nm order by cmte_nm"
>>> res1 = connection.execute(q1).fetchall()
>>> res1 != [(19920,), (38002,)]
True
>>> q2 = "select sum(transaction_amt) from joined where trial_id = 2 group by cmte_nm order by cmte_nm"
>>> res1 != connection.execute(q2).fetchall()
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