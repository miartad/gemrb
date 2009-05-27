#!/bin/bash
# GemRB - Infinity Engine Emulator
# Copyright (C) 2009 The GemRB Project
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# $Id$
#
# prepares NEWS for the restart of tracking bigger changes after release.

if [[ ! -e NEWS ]]; then
  echo 'Run me from the top gemrb dir that contains NEWS!'
  exit 3
fi

# get the last revision that contains a change in the word svn
# that's usually the final release update
rev=$(git log -Ssvn --pretty="format:%b" NEWS  | sed -n '1 s,^.*@\(\S*\) .*$,\1,p')
rev="${rev:-missing revision}"

cat - NEWS > NEWSNEWS << LILARCOR
GemRB svn ($rev):
  New features:
    - 

  Improved features:
    - 
    - various guiscripts
    - bugfixes

  Applied patches:

LILARCOR
mv NEWSNEWS NEWS
