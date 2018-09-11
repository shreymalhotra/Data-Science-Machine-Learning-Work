
test = {
  'name': 'q01e',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> np.allclose(model_2.coef_ , 0.70705475)
True
>>> np.allclose(model_3.coef_[1] , 0.21381339)
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
