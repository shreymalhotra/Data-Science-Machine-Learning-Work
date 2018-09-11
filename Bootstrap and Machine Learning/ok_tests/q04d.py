
test = {
  'name': 'q04d',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> isinstance(conf_interval_endpoints,tuple)
True
>>> len(conf_interval_endpoints) == 2
True
>>> conf_interval_endpoints[0] < conf_interval_endpoints[1]
True
>>> 
>>> conf_interval_endpoints[0] == np.percentile(boot_means,2.5)
True
>>> conf_interval_endpoints[1] == np.percentile(boot_means,97.5)
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
