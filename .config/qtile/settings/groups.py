from libqtile import extension
from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from libqtile.config import Group, Key, KeyChord


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
    Group(''),
    Group(name='separator', label='|'),
    Group(''),
    Group(boardG),
    Group(videoG, layout='max'),
    Group(radioG, layout='max'),
]

# more icons:    
# ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '. ''
