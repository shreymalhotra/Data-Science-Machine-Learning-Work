
test = {
  'name': 'q04c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> # also works with extremely high probability 
>>> max(boot_means) > np.mean(repair['time'])
True
>>> min(boot_means) < np.mean(repair['time'])
True
>>> abs(np.mean(boot_means) - np.mean(repair['time'])) < 0.1
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
