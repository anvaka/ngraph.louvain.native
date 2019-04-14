{
  'includes': [
    './common.gypi'
  ],
  'targets': [{
      'target_name': 'louvain',
      'type': 'executable',
      'sources': [
        './headers/community-graph.h',
        './src/community-graph.cc',
      ],
      'include_dirs': [
          './include'
      ],
      'all_dependent_settings': {
        'include_dirs': [
          './include'
        ],
      },
    },
  ]
}
