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

space1 = 'ﲋ'
space2 = ''
space3 = ''
space4 = '舘'
space5 = ''
space6 = '露'
groups = [
    Group(space1), # This icon is bugged
    Group(space2),
    Group(space3),
    Group(name='sep1', label=separator),
    Group(space4),
    Group(space5, layout='max'),
    Group(space6, layout='max'),
    Group(name='sep2', label=separator),
    Group(name='usual1', label=''),
    Group(name='usual2', label=''),
    Group(name='usual3', label=''),
    Group(name='usual4', label=''),
]

# more icons:    
# ' ', '', '', '', '', '', '', '', '', '', '', '', '', ''. '', ''
