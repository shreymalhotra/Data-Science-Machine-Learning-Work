
test = {
  'name': 'q05c',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> isinstance(punct_re, str)
True
>>> re.search(punct_re, 'this') is None
True
>>> re.search(punct_re, 'this is ok') is None
True
>>> re.search(punct_re, 'this is\nok') is None
True
>>> re.search(punct_re, 'this is not ok.') is not None
True
>>> re.search(punct_re, 'this#is#ok') is not None
True
>>> re.search(punct_re, 'this^is ok') is not None
True
>>> trump['no_punc'].loc['907588803161939968'] == 'fascinating to watch people writing books and major articles about me and yet they know nothing about me  amp  have zero access   fake news '
True
>>> trump['no_punc'].loc['907675638055743489'] == 'congratulations to eric  amp  lara on the birth of their son  eric  luke  trump this morning  https   t co aw0av82xde'
True
>>> # If you fail these tests, you accidentally changed the text column
>>> trump['text'].loc['907698529606541312'] == 'it was a great honor to welcome prime minister najib abdul razak of malaysia and his distinguished delegation to th… https://t.co/xihoapazpf'
True
>>> trump['text'].loc['884740553040175104'] == 'working hard to get the olympics for the united states (l.a.). stay tuned!'
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
