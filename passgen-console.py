#!/usr/bin/env python3

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

# Easy password settings
default_easy_size = 8
min_easy_size     = 6
max_easy_size     = 32

# Medium password settings
default_medium_size = 8
min_medium_size     = 6
max_medium_size     = 32

# Strong password settings
default_strong_size = 12
min_strong_size     = 6
max_strong_size     = 32

# --------------------------------------------------------------------------- #

usage = '''
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

about = '''
written by diSabler [Andy P. Gorelow]
mail: ..... dsy@dsy.name
site: ..... https://dsy.name
telegram: . https://t.me/disabler
(c) Disabler Production Lab.
'''

# --------------------------------------------------------------------------- #

def validate_passwd_length(current_len, default, min_size, max_size):
	'''
		Validate passwd type and length
	'''

	if current_len and current_len.isdigit():
		current_len = int(current_len)
	else:
		current_len = default

	if current_len < min_size:
		current_len = min_size
	elif current_len > max_size:
		current_len = max_size

	return current_len

def shuffle_chars(passwd):
	'''
		Shuffle password chars
	'''

	result = ''
	while passwd:
		result += passwd.pop(random.choice(range(0, len(passwd))))
	return result

def select_chars(chars, length):
	'''
		Select from chars list or lists
	'''

	result = []

	for idx in range(0, length):
		result.append(random.choice(chars[idx % len(chars)]))

	return result

def gen_chars(_from, _to, exclude = ''):
	'''
		Generate chars list with exclude
	'''
	return [chr(t) for t in range(ord(_from), ord(_to) + 1) if chr(t) not in exclude]

def get_passwd_simple(length):
	'''
		Simple password
	'''

	length = validate_passwd_length(length, default_easy_size, min_easy_size, max_easy_size)

	chars1 = list('aeiou')
	chars2 = gen_chars('a', 'z', chars1)

	result = ''
	begin = random.randint(0,1)

	for idx in range(0, length):
		if idx % 2 == begin:
			char = random.choice(chars2)
			if length <= 20:
				chars2.remove(char)
		else:
			char = random.choice(chars1)
			if length <= 10:
				chars1.remove(char)
		result += char

	return result

def get_passwd_medium(length):
	'''
		Medium password
	'''

	length = validate_passwd_length(length, default_medium_size, min_medium_size, max_medium_size)

	chars = [
		gen_chars('a', 'z', 'ilo'),
		gen_chars('A', 'Z', 'ILO'),
		gen_chars('2', '9'),
	]

	result = select_chars(chars, length)

	return shuffle_chars(result)

def get_passwd_strong(length):
	'''
		Strong password
	'''

	length = validate_passwd_length(length, default_strong_size, min_strong_size, max_strong_size)

	chars = [
		gen_chars('a', 'z', 'ilo'),
		gen_chars('A', 'Z', 'ILO'),
		gen_chars('2', '9'),
		list('!@$%^&*'),
	]

	result = select_chars(chars, length)

	return shuffle_chars(result)

def get_passwd_turn(source):
	'''
		Turn password EN-RU and RU-EN
	'''

	chars1 = '''`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'''
	chars2 = '''ё1234567890-=йцукенгшщзхъ\фывапролджэячсмитьбю.Ё!"№;%:?*()_+ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,'''

	turn1 = chars1 + chars2
	turn2 = chars2 + chars1

	result = ''.join([turn1[turn2.find(x)] if x in turn2 else x for x in source])

	return f'{source} = {result}'

def usage():
	'''
		Show usage
	'''
	return usage

def about():
	'''
		Show about me
	'''
	return about

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
			print(cmd(args[idx + 1]))
		else:
			print(cmd())
	else:
		match -= 1

if not match:
	print(usage())

# --- The end is near! ------------------------------------------------------ #
