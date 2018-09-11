
test = {
  'name': 'q06a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> isinstance(hash_re, str)
True
>>> re.search(rt_re, 'this') is None
True
>>> re.search(rt_re, 'this is the start.') is None
True
>>> re.search(rt_re, 'rt hi') is not None
True
>>> re.search(rt_re, 'hi rt') is not None
True
>>> re.search(rt_re, 'rt: hello') is not None
True
>>> re.search(rt_re, 'hello rt: @Sam') is not None
True
>>> re.search(hash_re, '# heya') is None
True
>>> re.search(hash_re, '#') is None
True
>>> re.search(hash_re, '#heya') is not None
True
>>> re.search(hash_re, '#h') is not None
True
>>> re.search(hash_re, 'ds100 is #goals') is not None
True
>>> re.search(hash_re, 'ds100 is # goals') is None
True
>>> re.search(hash_re, 'http://google.com') is not None
True
>>> re.search(hash_re, 'https://google.com') is not None
True
>>> re.search(hash_re, 'hihttphello') is not None
True
>>> 
>>> isinstance(hash_or_link, pd.DataFrame)
True
>>> # If you fail this test, you might not be looking everywhere in the string
>>> len(hash_or_link) > 1100
True
>>> '907303264458362880' in hash_or_link.index
True
>>> '907311779331690496' in hash_or_link.index
True
>>> '907588803161939968' in hash_or_link.index
True
>>> '907675638055743489' in hash_or_link.index
True
>>> '907698529606541312' in hash_or_link.index
True
>>> '906828550065582080' not in hash_or_link.index
True
>>> '906828871106002944' not in hash_or_link.index
True
>>> '906829008955957248' not in hash_or_link.index
True
>>> '907579024960098304' not in hash_or_link.index
True
>>> '907592460070768641' not in hash_or_link.index
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
