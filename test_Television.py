import pytest
from television import *
class Test:
    def setup_method(self):
        self.tv = Television()

    def test__init(self):
        assert self.tv.__str__() =="Power = False, Channel = 0, Volume = 0"

    def test__power(self):
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test__mute(self):
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv.power()
        self.tv.mute()
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 1"

    def test__channel_up(self):
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test__channel_down(self):
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test__volume_up(self):
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 2"
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test__volume_down(self):
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.volume_up()
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"


if __name__ == '__main__':
    pytest.main()