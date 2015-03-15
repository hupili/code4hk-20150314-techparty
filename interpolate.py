#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

order = 0
name = 'code4hk'

for line in sys.stdin.readlines():
    if line.startswith('##'):
        section = True
    else:
        section = False

    if section:
        sys.stdout.write('-----\n')

    sys.stdout.write(line)

    if section:
        sys.stdout.write('![](jpgs/%s-%s.jpg)\n' % (name, order))
        order += 1
