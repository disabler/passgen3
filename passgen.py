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

from PyQt5 import QtGui, Qt, QtWidgets

import random
import sys
import base64

# --- Base64 icons data ----------------------------------------------------- #

app_logo = '''
iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN
1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAIWSURBVEiJtVZL
iupQFCyfRqKE4EwDEkHEob/Bw0E7EtyGW9A1ZCRuwnU4EwTpxoDJUNToyAU4UGJi9aQNapKOynsFgaTu
uafO534CAB8APgHwHz+fAD5iPy9/EYFUKoVKpQKSME0Tp9MpagoAfCEqknq9ztlsRsdxeMX5fOZ0OmW1
Wn0mk/DBfr9P27Y9x67r0nVd79u2bfZ6vfcEWq0WL5cLSXI+n7PdblOSJEqSxE6nw8ViQZK8XC5stVqv
CQiCwNVqRZIcj8dMJBKBNpPJhCS5Wq0oCMLzArVazYuuUCiERlcul71y1Wq1QJs/Qa1vNBoAgPV6jd1u
F7pElsslttvt3ZxHBAqUSiUAwGazCXV+K3I75xGJR0JRFOTzeQCALMtoNpu/CsiyDADI5/NQFAX7/d5n
49VL07S79f4qHMehpmnBTU4mkzwcDm87v+JwODCZTPqbnE6nIUnSXWqGYaDb7aLb7cIwjEgeACRJQjqd
9pcok8n40lVV1YtEVVU6jhPK3yKTyfhL9Cig67pvTeu6Hsq/LGDbNrPZrGeYzWZp23Yo/7IASVqW5Z0/
lmVF8i8LkGQul2Mul3uafxQI3Mm3iMVib41d4dvJjxgOh3Bd18cPBgPE4/FIAeAnFVEUeTweA1N+Bcfj
kaIo+kt0Op0wGo2eiug3jEaju/vad+lXKhUUi8W3nG82G5imeUt9Af/5t+UbgPxVx4uuJ5AAAAAASUVO
RK5CYII='''

refresh_icon = '''
iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAB
2AAAAdgB+lymcgAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAIoSURBVEiJrda7
a1VBEAbw3x5uUFDE4AOE4AMRUSs1FmIp2Ih2WlgINgqBWNrlzxBBC7G2VARb0SZGBUElRfCBD1BBfCRK
fIzFbnS9OZckXAeG3WFnvm92zu7OSRGhl6SU1mMfhrG3jCvxEs9xDVcj4l1PkIiYp+hgDLOIBfQHLmFN
Fb8aIxExnwA7MN4C9AW3cBszLevvcRT78RDn5xHgJL5WQa9xGrvQVH4DpVxn8ary/1nFn/uHoGReg1/B
YFsJu5Jai5stOzr2h6DUvC7LiYWAK4JDmGohGK4JxurMlwA+io8t4J+xLCIkrJeP3QDeYFdEfOh16rol
pbQcO7G56Cb5KF/GZMJhXC/+ZyLi4mLBexBuw0Fsx2RHPg1zcqcf8CKBC2V+rZFvKEzjyX8gmMKnMt/S
+LuD+xHxq1/0yF//QTE3NlhRjL7BK2nKON3gRTF2p5RSv8gppQZ7ijnR4GkxVmFrvwTyizBXlXsd3JA/
zCT63gEOVPOJhHXymT0l38DnRZ/hcUR8WyxySmkQj7AB3zE0d+WXFfDuK/8Ro0t4Oq5UsWP1WzTcAj6F
Q0sAP1HFjqNTExxvIbiJtYsAHuzK/Ct2/FkvTueqxZ+V8yu5qQxjoAJt5CZ0Wm5KNfjJfxIoAeflNrdf
bnvvW3Y0I7fLW3L77F4frzPvJhjB6irDNXIj/9EC1K2zcj/ptJUwLfDbsg7HcER+54dK9hO4V8a7EfG2
F8ZvbEcQ+gUgivsAAAAASUVORK5CYII='''

exit_icon = '''
iVBORw0KGgoAAAANSUhEUgAAABIAAAAYCAYAAAD3Va0xAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN
1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAFeSURBVDiNrdW/
S1dhFMfx1zFrCPwRTiH+AKHd/8D2kLYK0fwPhGhoybXVNXBwdVLoH4iGmiNwiBRxsZwcFBrK0+Bz4Xr9
qvfm98DhPHDv876fc55zngv38RrfkR38AKt4kJngVUdA099lpsAPzGAbm9rbPF7gCONq5OeZqa3jaW3v
6EAHBddaa1BE3IuIJxExcisQVvABXyNiGof4+z+g8RKn8BG/8LKCDdbfjIgxbOFRD9BQbV3B5grsjNqp
YcHNfbNTNib2MZ2ZFxXhbol/8LaHqmOsYxnvK2URMddUtFzWv1v00VL5YOJzv/rorJlaZXci4k2L1Aaw
W7K5VbF3MVFNfx00hk/42cNPG8A9TBR1wxdANxR3rQGZxKLzhuw0tF9K3MdjPMRGqdOlPrrSMnMzInaw
l5mnETGrNmKtQQX27apnfbuPBp0f4QyeRUSXvfMlHuGEPl3+9Ol39A8h+wXnK6fPuwAAAABJRU5ErkJg
gg=='''

pass_easy = '''
iVBORw0KGgoAAAANSUhEUgAAABUAAAAYCAYAAAAVibZIAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN
1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAGXSURBVDiNrdQ/
axRBHMbxz08OD61E4ZSIbWysguBLSCEWwUoLLWzyWiRw2ApaSBpRQZADA2JhL/5BCL4ERdMIKjHeWNxc
nGx2x436wDCzs8/z3Z3Z32yklHQpIlawjPM4i/d4iWcppQedwZTSvoaTeIxUaRMstOZbgAv4UIR/4A0e
4jW2i3ufcKYPdFKEnuJ04/4pPCk9VSiulMtrW1rhfVR4r9ag69n0tfmGLdARvmT/eg26mU0vasDC/zz7
N8v5Q0X5HMFivnzVWS579Tb3izkPv6EYFtffekK/F5zhfHIQEQNcwsXCvBwRx3pALxTjtYiYmFWGsXqR
H7SNA59x3Kyo72Or18L3aoTLODzPz59ws+MLD7CCu7kfdPjWCtbuYLXD3NyeWx2+1bmn/Pr7FBFDXGtM
X4+Io7VcFYqfLZ7Azl9DU0o7ZssvNU4pbf/hZep7mvfrdvbcq3j67WmhrUZfVV/ogdQ8+12a/zhqP5rd
fGCa+3e4gY8doRNmp69NI9zBObn4N/zfs78BS3kw/UfYNHOWfgEJONhnVBmDMAAAAABJRU5ErkJggg==
'''

pass_medium = '''
iVBORw0KGgoAAAANSUhEUgAAABUAAAAYCAYAAAAVibZIAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN
1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAHOSURBVDiNrdUx
axZBEAbgZz9DQhoVlQRjEFHQJoXE/IcUYqGdpaiYf5JGSJlGOyuJRCIpIlbWiiiKxMZaUSGiMSGatbg9
mVzuPj7RgeVm33nnvZvb2d2Uc9ZlKaXLmMUMzmEdz7CWc17uTMw57xsYx0PkPmMFx1vzWwQn8CEk7+Al
lspzJ8Q+4eQgoqshaRUTjfiJBucJUqcorgbycltpgfsgcK/1E71XSJtd/ytwx/C18Jf6ib4tpKf9BAP/
ceG/j3gvtM8ozpbpi8522Ws171RK6VAN9gJhJMx/DCgaeaO1M5RSGsIlXAyE2ZTS4QFEZ4I/n1JawSNY
0L/J/3YsJHzGEWzjPr4M8IVNG8cVDNf59Rvmw6pOYRF3caGx4ucLvoipgN8OWn+cudB/2wH/hdMlNomf
IbaNsRKbq/G4+rVdL2XU1sOt4t/EgRAbLvw91ia60Qf71hJrw/aVfxSvAv5OOVRUJ9h6iL3RUv4+0SBc
42caCzUZYscC3vefwvcOv1lua+ldov9kQ8EfqZ2c81ZK6TkO4mMjZ0N1mm3mnLfa8hN2y/M1bqiuEqrW
6amuj7aPqXuYakfdUW2aDGv+795fg+ni7P6j2G7Rmf4N8ZHOlEqHOrUAAAAASUVORK5CYII='''

pass_strong = '''
iVBORw0KGgoAAAANSUhEUgAAABUAAAAYCAYAAAAVibZIAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN
1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAHpSURBVDiNrdW7
a1VBEAbw32rwYmEIClEiVmIsFAsR/BNSCIJYKQQsLS1sbSxSaMBCIjZapfEFgiQkKBZWwsUnYrCTdGJ8
kGAMhuRYnL1x7snJ9SpZGM7st998u7M7w0lFUdhopJROYQjHcBAf8AJPiqK4t2FgURTrDLvxEEUHm8BA
bXyN4AA+heBlvMF9vMavsDaHfd2IToSgKeytrO/Bo8jpKIozMb261AL3QeCe7SQ6nkmL1RPWiPZjIfPH
O4nOZNKzToKB/zTzZyK+JZTPdgzm6asNy6V9vM3fwRwPf0TRCPOfXYouBZ1GC+xJKW3FCZwM5KGUUl8X
oseDP5pSmlBWhis6F/m/2rWEL9ipLOo7+NpV4u2jH6exrRW/tgMOYSz7B/ILNzCsrMthNDK+H1dxE0cw
GrTWnMtYCfMl7ML1Snpj6MOPgK3iUp3o45r7uYhvFWw+41XudMuPJbVSc1eL+RQqvIUa7nLLiaJNzIb5
e9zFSCV4JOPvAjaL55HUOv4FZUe15r2hHW9k7HbAegN3EOfVpE95X+VORTFfg/9tHe3pb9roCX4Dn/HR
+gZ4qUytWcGbyl/PnND7Sfm6SflTO4fvyhdergjssP7Ve7L14hYO581N2tzen6ZssUnt3fQ/tpoFj/4G
ObPANtnn0J8AAAAASUVORK5CYII='''

about_icon = '''
iVBORw0KGgoAAAANSUhEUgAAABUAAAAYCAYAAAAVibZIAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN
1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAGMSURBVDiNtdU7
a1RREMDx34hCggo+mkAghUQI2BgRLQRFm1jFBRuDYGXjB5DoF7GwUjsRQbEIgpUgWEQsbERwg2ARRSzU
QjE4FnvEZblnN7vLDgyHef3PuXfOA/bgBjaQY+gH3Cw8q2PCenU18B6HcB+PjC7LWEFb1wytzDSqovWP
tWOMlVVl56CEiJjFAn5gIzM/D6qprjQiViLiHT7iGV7iU0SsRcT8SFBcxmG8xWO8Kf7zeBIRu/qBGxuF
RVzs8R3H75J/ZehGZebrzHzY41vHi2IeqdVup1FncA7z2PL/l80NDY2IGdzBUnH9wTfsK/Z0rbbx8yNi
Wqc5S3iFa5jNzP0690Rfqa30Ak7oHOGzmfm9K/ZrELTWqJNlXOsBbktq0C9lPNXtjIg5XC3mwWGhD/AT
ixHxNCKuR8QtrONAyTlajnCj1DZ/C1+74lu4h924W3y3mzZ/FVoS9+I0jmGqJzaDhSZo381fmvS8EtvE
ZlNsYvdpW+c5uRQRU2OwlsvYZgIPHxN4ov8C9W0iWxiu0LkAAAAASUVORK5CYII='''

info_icon = '''
iVBORw0KGgoAAAANSUhEUgAAABUAAAAYCAYAAAAVibZIAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN
1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAADoSURBVDiN7dU/
SkNBEMfxzwQLFb2AIIitvfaCbUippTewEKNHsrP2AOIdxCeWllqJBMfCFR7C821M0mXgxzLszHdn2T8D
G7jEE3IGPeOq8IxnhP3WOPCIXVzjxv9tiBM0WiuMMlOXsIUjRMf86Ic1qCkhIga4wy1O++KroJn5ibfi
vvbFr9RAi+1jOzMf5gbNzHf0AqnYfkScRcR9S3t9OTWV7uCg5W/2JdQc1DnW8FIRi4pKM3OCSUTUMuuu
1LS2hC6hc7ZpfqkLrCs/ex+08d1OjiNi9Y/Yj6LDjtc1LGPDAhofC2jRX3cXmLp2Hb/fAAAAAElFTkSu
QmCC'''

# --------------------------------------------------------------------------- #

min_easy_size = 6
max_easy_size = 32

min_medium_size = 6
max_medium_size = 32

min_strong_size = 6
max_strong_size = 32

# --------------------------------------------------------------------------- #

passwd_style      = 'font-size: 12pt; font-family: Courier; height: 26px;'
passwdlen_style   = 'font-size: 12pt; font-family: Courier; height: 26px; width: 100%;'
exit_button_style = 'font-size: 12pt; font-family: Courier; height: 26px;'

# --------------------------------------------------------------------------- #

simple_shortcut = 'Ctrl+1'
medium_shortcut = 'Ctrl+2'
strong_shortcut = 'Ctrl+3'
turn_shortcut   = 'Ctrl+4'
help_shortcut   = 'Ctrl+J'
about_shortcut  = 'Ctrl+I'
exit_shortcut   = 'Ctrl+Q'

windows_title = 'Password Generator'

help_text = '''<hr />
<p><i>Generate password and copy to clipboard:</i></p>
<p><b>%(meta)s1 ... <font color="#ff0000">Simple:</font></b> For typing by hand.</p>
<p><b>%(meta)s2 ... <font color="#ffe900">Medium:</font></b> Contain chars, CHARS, numbers. Excluded similar by writing i, l, o, I, L, O, 1, 0.</p>
<p><b>%(meta)s3 ... <font color="#00bd00">Strong:</font></b> Contain chars, CHARS, numbers, symbols. Excluded similar by writing i, l, o, I, L, O, 1, 0.</p>
<p><b>%(meta)s4 ... <font color="#0a0a0a">Turn:</font></b> Turn layout EN-RU and RU-EN. Easy for remember, hard for guess.</p>
<hr />
<p><i>Other keys:</i></p>
<p><b>%(meta)sI ... About me:</b> Show infromation about me.</p>
<p><b>%(meta)sJ ... Help:</b> This window.</p>
<p><b>%(meta)sQ ... Quit:</b> Exit application.</p>
'''

about_text = '''<hr />
<table><tbody>
<tr>
  <td>nick</td>
  <td align="right"><a style="font-weight:bold;"
      href="https://dsy.name">diSabler</a></td>
</tr>
<tr>
  <td>name</td>
  <td align="right"><a style="font-weight:bold;"
      href="https://dsy.name">Andy P. Gorelow</a></td>
</tr>
<tr>
  <td>e-mail</td>
  <td align="right"><a style="font-weight:bold;"
      href="mailto:dsy@dsy.name">dsy@dsy.name</a></td>
</tr>
<tr>
  <td>telegram</td>
  <td align="right"><a style="font-weight:bold;"
      href="http://t.me/disabler">@disabler</a></td>
</tr>
</tbody></table>
<hr />
<i>&copy; Disabler Production Lab.</i>
'''

# --------------------------------------------------------------------------- #

def gen_chars(_from, _to, exclude = ''):
	'''
		Generate chars list with exclude
	'''
	return [chr(t) for t in range(ord(_from), ord(_to) + 1) if chr(t) not in exclude]

def validate_passwd_length(current_len, min_size, max_size):
	'''
		Validate passwd type and length
	'''

	if current_len and current_len.isdigit():
		current_len = int(current_len)
	else:
		current_len = -1

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

# --------------------------------------------------------------------------- #

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		self.clipboard = QtWidgets.QApplication.clipboard()
		QtWidgets.QMainWindow.__init__(self, parent)

		# Main window
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(app_logo))
		self.setWindowIcon(Qt.QIcon(m_ico))
		self.setWindowTitle(windows_title)
		self.resize(440, 100)
		self.window = Qt.QWidget()
		self.layout_main = Qt.QGridLayout()
		self.layout_main.setContentsMargins(8, 4, 4, 8)
		self.layout_main.setSpacing(3)
		self.window.setLayout(self.layout_main)

		# Simple password
		lbl1 = QtWidgets.QLabel()
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(pass_easy))
		lbl1.setPixmap(QtGui.QPixmap(m_ico))
		self.textPasswd1 = Qt.QLineEdit()
		self.textPasswd1.setStyleSheet(passwd_style)
		self.textPasswd1Len = Qt.QLineEdit()
		self.textPasswd1Len.setStyleSheet(passwdlen_style)
		self.textPasswd1Len.setText('8')
		self.textPasswd1Len.setFixedWidth(29)
		self.textPasswd1Len.setValidator(Qt.QIntValidator(min_easy_size, max_easy_size))
		self.textPasswd1Len.textChanged.connect(self.get_passwd_simple)
		self.layout_main.addWidget(lbl1, 0, 0)
		self.layout_main.addWidget(self.textPasswd1, 0, 1)
		self.layout_main.addWidget(self.textPasswd1Len,0, 2)
		new_menu1 = QtWidgets.QAction(QtGui.QIcon(m_ico), 'Refresh simple password', self)
		new_menu1.setShortcut(simple_shortcut)
		new_menu1.triggered.connect(self.get_passwd_simple)
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(refresh_icon))
		new_act1 = QtWidgets.QPushButton()
		new_act1.setIcon(QtGui.QIcon(m_ico))
		new_act1.setIconSize(m_ico.rect().size())
		self.layout_main.addWidget(new_act1, 0, 3)
		new_act1.clicked.connect(self.get_passwd_simple)

		# Medium password
		lbl2 = QtWidgets.QLabel()
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(pass_medium))
		lbl2.setPixmap(QtGui.QPixmap(m_ico))
		self.textPasswd2 = Qt.QLineEdit()
		self.textPasswd2.setStyleSheet(passwd_style)
		self.textPasswd2Len = Qt.QLineEdit()
		self.textPasswd2Len.setStyleSheet(passwdlen_style)
		self.textPasswd2Len.setText('12')
		self.textPasswd2Len.setFixedWidth(29)
		self.textPasswd2Len.setValidator(Qt.QIntValidator(min_medium_size, max_medium_size))
		self.textPasswd2Len.textChanged.connect(self.get_passwd_medium)
		self.get_passwd_medium()
		self.layout_main.addWidget(lbl2, 1, 0)
		self.layout_main.addWidget(self.textPasswd2, 1, 1)
		self.layout_main.addWidget(self.textPasswd2Len, 1, 2)
		new_menu2 = QtWidgets.QAction(QtGui.QIcon(m_ico), 'Refresh medium password', self)
		new_menu2.setShortcut(medium_shortcut)
		new_menu2.triggered.connect(self.get_passwd_medium)
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(refresh_icon))
		new_act2 = QtWidgets.QPushButton()
		new_act2.setIcon(QtGui.QIcon(m_ico))
		new_act2.setIconSize(m_ico.rect().size())
		self.layout_main.addWidget(new_act2, 1, 3)
		new_act2.clicked.connect(self.get_passwd_medium)

		# Strong password
		lbl3 = QtWidgets.QLabel()
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(pass_strong))
		lbl3.setPixmap(QtGui.QPixmap(m_ico))
		self.textPasswd3 = Qt.QLineEdit()
		self.textPasswd3.setStyleSheet(passwd_style)
		self.textPasswd3Len = Qt.QLineEdit()
		self.textPasswd3Len.setStyleSheet(passwdlen_style)
		self.textPasswd3Len.setText('24')
		self.textPasswd3Len.setFixedWidth(29)
		self.textPasswd3Len.setValidator(Qt.QIntValidator(min_strong_size, max_strong_size))
		self.textPasswd3Len.textChanged.connect(self.get_passwd_strong)
		self.get_passwd_strong()
		self.layout_main.addWidget(lbl3, 2, 0)
		self.layout_main.addWidget(self.textPasswd3, 2, 1)
		self.layout_main.addWidget(self.textPasswd3Len, 2, 2)
		new_menu3 = QtWidgets.QAction(QtGui.QIcon(m_ico), 'Refresh strong password', self)
		new_menu3.setShortcut(strong_shortcut)
		new_menu3.triggered.connect(self.get_passwd_strong)
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(refresh_icon))
		new_act3 = QtWidgets.QPushButton()
		new_act3.setIcon(QtGui.QIcon(m_ico))
		new_act3.setIconSize(m_ico.rect().size())
		self.layout_main.addWidget(new_act3, 2, 3)
		new_act3.clicked.connect(self.get_passwd_strong)

		# Turn password
		lbl4 = QtWidgets.QLabel()
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(refresh_icon))
		lbl4.setPixmap(QtGui.QPixmap(m_ico))
		self.textPasswd4 = Qt.QLineEdit()
		self.textPasswd4.setStyleSheet(passwd_style)
		self.textPasswd4.setText('example_text_to_turn')
		self.layout_main.addWidget(lbl4, 3, 0)
		self.layout_main.addWidget(self.textPasswd4, 3, 1)
		new_menu4 = QtWidgets.QAction(QtGui.QIcon(m_ico), 'Update `turn` password', self)
		new_menu4.setShortcut(turn_shortcut)
		new_menu4.triggered.connect(self.get_passwd_turn)
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(refresh_icon))
		new_act4 = QtWidgets.QPushButton()
		new_act4.setIcon(QtGui.QIcon(m_ico))
		new_act4.setIconSize(m_ico.rect().size())
		self.layout_main.addWidget(new_act4, 3, 3)
		new_act4.clicked.connect(self.get_passwd_turn)

		# Quit button
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(exit_icon))
		quit_act = QtWidgets.QPushButton()
		quit_act.setIcon(QtGui.QIcon(m_ico))
		quit_act.setIconSize(m_ico.rect().size())
		quit_act.setStyleSheet(exit_button_style)
		self.layout_main.addWidget(quit_act,4,0,1,4)
		quit_act.clicked.connect(self.close)
		exit_menu = QtWidgets.QAction(QtGui.QIcon(m_ico), 'Quit', self)
		exit_menu.setShortcut(exit_shortcut)
		exit_menu.triggered.connect(self.close)

		# Help shortcut
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(info_icon))
		help_menu = QtWidgets.QAction(QtGui.QIcon(m_ico), 'Help', self)
		help_menu.setShortcut(help_shortcut)
		help_menu.triggered.connect(self.help_info)

		# About me shortcut
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(about_icon))
		about_menu = QtWidgets.QAction(QtGui.QIcon(m_ico), 'About me', self)
		about_menu.setShortcut(about_shortcut)
		about_menu.triggered.connect(self.about_info)

		# Menu bar
		self.setCentralWidget(self.window)

		self.get_passwd_simple()

		menubar = self.menuBar()

		menu_f = menubar.addMenu('&Menu')
		menu_f.addAction(new_menu1)
		menu_f.addAction(new_menu2)
		menu_f.addAction(new_menu3)
		menu_f.addAction(new_menu4)
		menu_f.addSeparator()
		menu_f.addAction(exit_menu)

		menu_h = menubar.addMenu('&Help')
		menu_h.addAction(help_menu)
		menu_h.addAction(about_menu)

	def show_box(self, title, body, icon):
		'''
			Show window box
		'''
		msgBox = QtWidgets.QMessageBox()
		msgBox.setWindowTitle(windows_title)
		msgBox.setText('<h2><strong>%s</strong></h2>' % title)
		msgBox.setInformativeText(body)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(icon))
		msgBox.setIconPixmap(m_ico)
		m_ico = QtGui.QPixmap()
		m_ico.loadFromData(base64.b64decode(app_logo))
		msgBox.setWindowIcon(Qt.QIcon(m_ico))
		msgBox.resize(600, 100)
		msgBox.exec_()

	def help_info(self):
		'''
			Show help
		'''
		self.show_box('Help', help_text % self.get_meta_symbol(), info_icon)

	def about_info(self):
		'''
			Show about me
		'''
		self.show_box('About me', about_text, about_icon)

	def get_passwd_simple(self):
		'''
			Simple password
		'''

		length = validate_passwd_length(self.textPasswd1Len.text(), min_easy_size, max_easy_size)

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

		self.clipboard.setText(result)
		self.textPasswd1.setText(result)

	def get_passwd_medium(self):
		'''
			Medium password
		'''

		length = validate_passwd_length(self.textPasswd2Len.text(), min_medium_size, max_medium_size)

		chars = [
			gen_chars('a', 'z', 'ilo'),
			gen_chars('A', 'Z', 'ILO'),
			gen_chars('2', '9'),
		]

		result = select_chars(chars, length)
		result = shuffle_chars(result)

		self.clipboard.setText(result)
		self.textPasswd2.setText(result)

	def get_passwd_strong(self):
		'''
			Strong password
		'''

		length = validate_passwd_length(self.textPasswd3Len.text(), min_strong_size, max_strong_size)

		chars = [
			gen_chars('a', 'z', 'ilo'),
			gen_chars('A', 'Z', 'ILO'),
			gen_chars('2', '9'),
			list('!@$%^&*'),
		]

		result = select_chars(chars, length)
		result = shuffle_chars(result)

		self.clipboard.setText(result)
		self.textPasswd3.setText(result)

	def get_passwd_turn(self):
		'''
			Turn password EN-RU and RU-EN
		'''

		chars1 = '''`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'''
		chars2 = '''ё1234567890-=йцукенгшщзхъ\фывапролджэячсмитьбю.Ё!"№;%:?*()_+ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,'''

		turn1 = chars1 + chars2
		turn2 = chars2 + chars1

		source = str(self.textPasswd4.text())
		result = ''.join([turn1[turn2.find(x)] if x in turn2 else x for x in source])

		self.clipboard.setText(result)
		self.textPasswd4.setText(result)

	def get_meta_symbol(self):
		'''
			Choice metasymbol for MacOS and other
		'''
		if sys.platform == 'darwin':
			return { 'meta' : '⌘' }
		else:
			return { 'meta' : '^' }

# --------------------------------------------------------------------------- #

if __name__ == '__main__' :
	app = QtWidgets.QApplication(sys.argv)
	app.setApplicationName(windows_title)
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())

# --- The end is near! ------------------------------------------------------ #
