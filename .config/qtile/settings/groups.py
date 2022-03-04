from libqtile import extension
from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from libqtile.config import Group, Key, KeyChord

separator = ''

# G of Group
boardG = '舘' #    舘 
videoG = '' # 
radioG = '露' # 鷺 露 蓼
# musicG = ' ' #  
# groups = [Group(i) for i in [' ', boardG, ' ', ' ', ' ', videoG, radioG, musicG]]
groups = [
    Group('ﲋ'), # This icon is bugged
    Group(''),
    Group(''),
    Group(name='sep1', label=separator),
    Group(boardG),
    Group(videoG, layout='max'),
    Group(radioG, layout='max'),
    Group(name='sep2', label=separator),
    Group(''),
    Group(''),
    Group(name='sep3', label=separator),
    Group(''),
    Group(''),
]

# more icons:    
# ' ', '', '', '', '', ' ', ' ', ' ', ' ', ' ', ' ', '', '', ''. ''
