test = {
  'name': 'Question 4b',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> bus_sf_latlong.shape == (24,3)
          True
          >>> np.allclose(bus_sf_latlong['null_lon'].mean(), 103.5416)
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
