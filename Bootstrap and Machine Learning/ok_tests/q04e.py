
test = {
  'name': 'q04e',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> # essentially equivalent to the test in 4d 
>>> # if the studentization was done correctly
>>> abs(np.mean(boot_stu_means)) < 0.1
True
>>> len(boot_stu_means) == 10000
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
