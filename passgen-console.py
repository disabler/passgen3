#!/usr/local/bin/python3

# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
#                                                                             #
#    Password Generator                                                       #
#    Copyright (C) diSabler <dsy@dsy.name>                                    #
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                             #
# --------------------------------------------------------------------------- #

import random
import sys

# --------------------------------------------------------------------------- #

MIN_EASY_SIZE = 6
MAX_EASY_SIZE = 32
DEFAULT_EASY_SIZE = 8

MIN_MEDIUM_SIZE = 6
MAX_MEDIUM_SIZE = 32
DEFAULT_MEDIUM_SIZE = 8

MIN_STRONG_SIZE = 6
MAX_STRONG_SIZE = 32
DEFAULT_STRONG_SIZE = 12

# --------------------------------------------------------------------------- #

USAGE = '''
Generate password:
-e, --easy ... For typing by hand.
-m, --medium . Contain chars, CHARS, numbers. Excluded similar by writing i, l, o, I, L, O, 1, 0.
-s, --strong . Contain chars, CHARS, numbers, symbols. Excluded similar by writing i, l, o, I, L, O, 1, 0.
-t, --turn ... Turn layout EN-RU and RU-EN. Easy for remember, hard for guess.
-a, --about .. About me.
-h, --help ... This text.

Usage:
passgen [type] [password len]

Example:
passgen --easy 10 -e 14 --medium --strong
'''

ABOUT = '''
written by diSabler [Andy P. Gorelow]
mail: ..... dsy@dsy.name
site: ..... https://dsy.name
telegram: . https://t.me/disabler
donate: ... https://www.paypal.me/dissy
(c) Disabler Production Lab.
'''

# --------------------------------------------------------------------------- #

def get_passwd_simple(LEN):
	if LEN and LEN.isdigit():
		LEN = int(LEN)
	else:
		LEN = DEFAULT_EASY_SIZE
	L1 = ['a','e','i','o','u']
	L2 = [chr(t) for t in range(ord('a'),ord('z')+1) if chr(t) not in L1]
	PASS = ''
	if LEN < MIN_EASY_SIZE:
		LEN = MIN_EASY_SIZE
	elif LEN > MAX_EASY_SIZE:
		LEN = MAX_EASY_SIZE
	BEG = random.randint(0,1)

	for t in range(0,LEN):
		if t % 2 == BEG:
			LIT = random.choice(L2)
			if LEN <= 20:
				L2.remove(LIT)
		else:
			LIT = random.choice(L1)
			if LEN <= 10:
				L1.remove(LIT)
		PASS += LIT
	return PASS

def get_passwd_medium(LEN):
	if LEN and LEN.isdigit():
		LEN = int(LEN)
	else:
		LEN = DEFAULT_MEDIUM_SIZE
	RND1 = [chr(t) for t in range(ord('a'),ord('z')+1) if chr(t) not in 'ilo']
	RND2 = [chr(t) for t in range(ord('A'),ord('Z')+1) if chr(t) not in 'ILO']
	RND3 = [chr(t) for t in range(ord('2'),ord('9')+1)]

	if LEN < MIN_MEDIUM_SIZE:
		LEN = MIN_MEDIUM_SIZE
	elif LEN > MAX_MEDIUM_SIZE:
		LEN = MAX_MEDIUM_SIZE

	RND_T = [RND1,RND2,RND3]
	IDX = 0
	PRE = []

	for t in range(0,LEN):
		PRE += [random.choice(RND_T[IDX])]
		IDX += 1
		if IDX >= len(RND_T): IDX = 0
	REZ = ''
	while PRE:
		REZ += PRE.pop(random.choice(range(0,len(PRE))))
	return REZ

def get_passwd_strong(LEN):
	if LEN and LEN.isdigit():
		LEN = int(LEN)
	else:
		LEN = DEFAULT_STRONG_SIZE
	RND1 = [chr(t) for t in range(ord('a'),ord('z')+1) if chr(t) not in 'ilo']
	RND2 = [chr(t) for t in range(ord('A'),ord('Z')+1) if chr(t) not in 'ILO']
	RND3 = [chr(t) for t in range(ord('2'),ord('9')+1)]
	RND4 = list('!@$%^&*')

	if LEN < MIN_STRONG_SIZE:
		LEN = MIN_STRONG_SIZE
	elif LEN > MAX_STRONG_SIZE:
		LEN = MAX_STRONG_SIZE

	RND_T = [RND1,RND2,RND3,RND4]
	IDX = 0
	PRE = []

	for t in range(0,LEN):
		PRE += [random.choice(RND_T[IDX])]
		IDX += 1
		if IDX >= len(RND_T): IDX = 0
	REZ = ''
	while PRE:
		REZ += PRE.pop(random.choice(range(0,len(PRE))))
	return REZ

def get_passwd_turn(TEXT):
	T1 = '''`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'''
	T2 = '''ё1234567890-=йцукенгшщзхъ\фывапролджэячсмитьбю.Ё!"№;%:?*()_+ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,'''
	TURN1 = T1 + T2
	TURN2 = T2 + T1
	REZ = ''.join([TURN1[TURN2.find(x)] if x in TURN2 else x for x in TEXT])
	return '%s = %s' % (TEXT, REZ)

def usage(_):
	return USAGE

def about(_):
	return ABOUT

# --------------------------------------------------------------------------- #

OPTS =	{
		'-e':		[get_passwd_simple, 1],
		'--easy':	[get_passwd_simple, 1],
		'-m':		[get_passwd_medium, 1],
		'--medium':	[get_passwd_medium, 1],
		'-s':		[get_passwd_strong, 1],
		'--strong':	[get_passwd_strong, 1],
		'-t':		[get_passwd_turn, 1],
		'--turn':	[get_passwd_turn, 1],
		'-h':		[usage, 0],
		'--help':	[usage, 0],
		'-a':		[about, 0],
		'--about':	[about, 0]
		}

args = sys.argv[1:]

match = len(args)
for idx in range(0, len(args)):
	if args[idx] in OPTS:
		cmd, cmd_len = OPTS[args[idx]]
		if cmd_len and idx + 1 < len(args):
			param = args[idx + 1]
		else:
			param = ''
		print(cmd(param))
	else:
		match -= 1

if not match:
	print(usage(''))

# --- The end is near! ------------------------------------------------------ #
