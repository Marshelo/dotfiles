from libqtile import extension
from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from libqtile.config import Group, Key, KeyChord

separator = '|'

# G of Group
# boardG =  #     
# videoG =  # 
# radioG =  # 鷺 露 蓼
# musicG = ' ' #  
# groups = [Group(i) for i in [' ', boardG, ' ', ' ', ' ', videoG, radioG, musicG]]
#      
#           
space = [
    '', '', '',
    '', '', '',
    '', '', '',]
groups = [
    Group(space[0]), # Common groups
    Group(space[1]),
    Group(space[2]),
    Group(name='sep1', label=separator),
    Group(space[3]), # Hot groups area
    Group(space[4]),
    Group(space[5]),
    Group(name='sep2', label=separator),
    Group(space[6]), # Secondaries necessities groups
    Group(space[7]),
    Group(space[8]),
]

# more icons:   
# 'ﲋ', '', '', '舘','', '露', '', '', '', '', '', '', '', '', '', '', ''. '', '', ''
# Figures:  '', 'ﱢ', '卑', '', '', '爫',