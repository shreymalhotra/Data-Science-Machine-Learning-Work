
test = {
  'name': 'q05e',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> np.allclose(polarities.loc['907698529606541312', 'polarity'], 7.3)
True
>>> np.allclose(polarities.loc['907675638055743489', 'polarity'], 2.9)
True
>>> np.allclose(polarities.loc['907592460070768641', 'polarity'], 3.2)
True
>>> np.allclose(polarities.loc['907588803161939968', 'polarity'], 0.4)
True
>>> np.allclose(polarities.loc['907579024960098304', 'polarity'], 4.7)
True
>>> # If you fail this test, you dropped tweets with 0 polarity
>>> np.allclose(polarities.loc['907303264458362880', 'polarity'], 0.0)
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
