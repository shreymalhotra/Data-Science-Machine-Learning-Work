test = {
  'name': 'Question 3b',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> zip_counts["count"].sum()
          6315
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(zip_counts.index) == {'00000', '92672', '94013', '94014', '94066', '941', '94101', '94102', '94103', '941033148', '94104', '94105', '94107', '94108', '94109', '94110', '941102019', '94111', '94112', '94114', '94115', '94116', '94117', '94118', '94120', '94121', '94122', '94123', '94124', '94127', '94129', '94130', '94131', '94132', '94133', '94134', '94143', '94158', '94188', '94545', '94602', '94609', '94621', '95105', 'CA', 'Ca', 'MISSING'}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> zip_counts.columns.values[0] == "count"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> zip_counts.shape[1]
          1
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
