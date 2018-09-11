
test = {
  'name': 'q02c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> np.allclose(conf_interval_exact, (-18/7, 88/7))
True
>>> np.allclose(conf_interval_exact[1] - conf_interval_sim[1], 0.0)
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
