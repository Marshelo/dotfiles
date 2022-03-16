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


space1 = ''
space2 = '卑'
space3 = 'ﱢ'
space4 = 'ﴯ'
space5 = ''
space6 = '露'
space7 = ''
space8 = ''
space9 = '爫'
groups = [
    Group(space1), # Common groups
    Group(space2),
    Group(space3),
    Group(name='sep1', label=separator),
    Group(space4, layout='max'), # Hot groups area
    Group(space5, layout='max'),
    Group(name='sep2', label=separator),
    Group(space6), # Secondaries necessities groups
    Group(space7),
    Group(space8),
    Group(space9),
]

# more icons:    
# 'ﲋ', '', '', '舘','', '露', '', '', '', '', '', '', '', '', '', '', ''. '', '', ''
