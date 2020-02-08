"""This module is created by PRO, aiming at making it easier for termux users to use android API.
Please install 'Termux: API' app on your phone and 'termux-api' package on termux before using this module.
For more help, use help(xxx)."""

from os import popen
class MediaPlayer:
    """Introduction: Play media via python on termux."""
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