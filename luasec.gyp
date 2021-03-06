# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'luasec',
      'type': 'shared_library',
      'product_dir': "<(PRODUCT_DIR)",
      'product_name': 'ssl',
      'sources': [
        'src/x509.c',
        'src/context.c',
        'src/ssl.c',
        'src/luasocket/buffer.c',
        'src/luasocket/io.c',
        'src/luasocket/timeout.c'
      ],
      'include_dirs': [
        '.',
        'src',
        '<(DEPTH)/third_party/lua/src',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/lua/lua.gyp:liblua',
        '<(DEPTH)/third_party/openssl/openssl.gyp:openssl'
      ],
      'direct_dependent_settings': {
      },
      'copies': [
        { 'destination': '<(PRODUCT_DIR)',
          'files': [
            'src/ssl.lua'
        ]},
        { 'destination': '<(PRODUCT_DIR)/ssl',
          'files': [
            'src/https.lua'
        ]},
      ],  
      'conditions': [
        ['OS=="linux"', {
          'product_prefix': '',
          'cflags!': ['-fvisibility=hidden'],
          'sources': [
            'src/luasocket/usocket.c'
          ],
        }], 
        ['OS == "mac"', {
          'product_prefix': '',
          'product_extension': 'so',
          'xcode_settings': {
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'NO',
          },
          'sources': [
            'src/luasocket/usocket.c'
          ],
        }],
        ['OS=="win"', {
          'defines': [
            '_USRDLL',
            'LUASEC_EXPORTS',
            '_WIN32',
          ],
          'sources': [
            'src/luasocket/wsocket.c'
          ],
        }],
      ],
    },
  ]
}
