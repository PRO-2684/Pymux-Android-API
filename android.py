"""This module is created by PRO-2684, aiming at making it easier for termux users to use android API via python.
Please install 'Termux: API' app on your phone and 'termux-api' package on termux before using this module.
For more help, use help(xxx).
此模块由PRO-2684创建，旨在让termux用户更方便地在python中使用Android API。
请先安装与Termux同来源的'Termux: API' app，并在Termux中安装termux-api包后再使用。
更多帮助请使用 help(xxx)。
"""

from os import popen
class MediaPlayer:
    """Introduction: Used to play media."""
    def play(path=''):
        """Takes one or zero argument.
        If an argument is given, it will play the media at specified path.
        Else, it will try to resume the paused media."""
        return popen('termux-media-player play '+path).read()
    def pause():
        """Pause."""
        return popen('termux-media-player pause ').read()
    def stop():
        """Stop playing."""
        return popen('termux-media-player stop').read()
    def info():
        """Return infomation about the media played now."""
        return popen('termux-media-player info').read()

class Location:
    """Introduction: Output your location. Support:
    1. Network location.
    2. GPS location.
    3. Passive location."""
    def network():
        """Return your location based on network."""
        return popen('termux-location -p network').read()
    def gps():
        """Return your location based on GPS."""
        return popen('termux-location -p gps').read()
    def passive():
        """Return your location based on passive."""
        return popen('termux-location -p passive').read()

class Clipboard:
    """Some operation on clipboard."""
    def get():
        """Return current clipboard content."""
        return popen('termux-clipboard-get').read()
    def set(string):
        """Set clipboard."""
        popen('termux-clipboard-set '+m)

class Toast:
    """Show toast."""
    def __init__(self,message,bg_color='',txt_color='',pos=''):
        """Initiation.
        '*_color' argument can be a standard name(i.e. 'red', 'grey') or 6/8 digit value(i.e.'#FF0000' or '#FFFF0000'), where order is (AA)RRGGBB.(AA means transparency.)
        'pos' argument can be one of the following: 'top', 'middle', 'bottom'.
        Invalid arguments will revert to default value(grey, white, middle)."""
        self.message=message
        self.bg_color=bg_color
        self.txt_color=txt_color
        self.pos=pos
    def show(self):
        """Show toast"""
        settings=''
        if self.bg_color: settings+=f'-b "{self.bg_color}" '
        if self.txt_color: settings+=f'-c "{self.txt_color}" '
        if self.pos: settings+=f'-g {self.pos} '
        popen('termux-toast '+settings+self.message)
