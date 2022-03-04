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
groups = [
    Group('ﲋ'), # This icon is bugged
    Group(''),
    Group(''),
    Group(name='sep1', label=separator),
    Group('舘'),
    Group('', layout='max'),
    Group('露', layout='max'),
    Group(name='sep2', label=separator),
    Group(name='usual1', label=''),
    Group(name='usual2', label=''),
    Group(name='usual3', label=''),
    Group(name='usual4', label=''),
]

# more icons:    
# ' ', '', '', '', '', '', '', '', '', '', '', '', '', ''. '', ''
