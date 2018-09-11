test = {
  'name': 'Question 7a',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all(len(v[0])==2 for v in scores_pairs_by_business.values)
          True
          >>> scores_pairs_by_business['score_pair'][24] == [96,98]
          True
          >>> scores_pairs_by_business['score_pair'][323] == [100,94]
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
