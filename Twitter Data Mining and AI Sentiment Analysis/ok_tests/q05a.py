
test = {
  'name': 'q05a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> isinstance(sent, pd.DataFrame)
True
>>> sent.shape == (7517, 1)
True
>>> list(sent.index[5000:5005]) == ['paranoids', 'pardon', 'pardoned', 'pardoning', 'pardons']
True
>>> np.allclose(sent['polarity'].head(), [-1.5, -0.4, -1.5, -0.4, -0.7])
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
