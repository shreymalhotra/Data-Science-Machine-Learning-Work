
test = {
  'name': 'q05d',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> abs(np.mean(b_strata) - weighted_sample_avg) < 0.005
True
>>> abs(np.mean(b_simple) - sample_avg) < 0.005
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
