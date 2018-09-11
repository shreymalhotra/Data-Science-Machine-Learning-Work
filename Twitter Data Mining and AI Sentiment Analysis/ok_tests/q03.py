
test = {
  'name': 'q03',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> isinstance(trump, pd.DataFrame)
True
>>> trump.shape[0] < 3300
True
>>> trump.shape[1] >= 4
True
>>> '907698529606541312' in trump.index
True
>>> '907675638055743489' in trump.index
True
>>> all(col in trump.columns for col in ['time', 'source', 'text', 'retweet_count'])
True
>>> # If you fail these tests, you probably tried to use __dict__ or _json to read in the tweets
>>> 'Twitter for iPhone' in trump['source'].values
True
>>> trump['time'].dtype == np.dtype('<M8[ns]')
True
>>> trump['text'].dtype == np.dtype('O')
True
>>> trump['retweet_count'].dtype == np.dtype('int64')
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
