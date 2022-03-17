from libqtile import extension
from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from libqtile.config import Group, Key, KeyChord

separator = '|'

# G of Group
# boardG =  #    舘 
# videoG =  # 
# radioG =  # 鷺 露 蓼
# musicG = ' ' #  
# groups = [Group(i) for i in [' ', boardG, ' ', ' ', ' ', videoG, radioG, musicG]]

space = [
    'ﲋ', '', '',
    '', '卑', 'ﱢ',
    '', '', '爫',]
groups = [
    Group(space[0]), # Common groups
    Group(space[1]),
    Group(space[2]),
    Group(name='sep1', label=separator),
    Group(space[3], layout='max'), # Hot groups area
    Group(space[4]),
    Group(space[5], layout='max'),
    Group(name='sep2', label=separator),
    Group(space[6]), # Secondaries necessities groups
    Group(space[7]),
    Group(space[8]),
]

# more icons:    
# 'ﲋ', '', '', '舘','', '露', '', '', '', '', '', '', '', '', '', '', ''. '', '', ''
