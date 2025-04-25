class Television:
    "these are the constant TV Variables"
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        "This is the instance variables that the Methods will refer to when changing one."
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL
    def power(self)->None:
        "This Returns true if the power is on and false when not"
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    def mute(self)->None:
        "this will change true if the volume is muted"
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True
    def channel_up(self)->None:
        "this will increase the channel number unless it is already the max then it will be set to min"
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel +=1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self)->None:
        "this will decrease the channel number as long as it isn't the min channel it will decrease else it will set it to max"
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel-=1
            else:
                self.__channel = Television.MAX_CHANNEL
    def volume_up(self)->None:
        "this will increase the as long as it isn't the max volume"
        if self.__status:
            self.__muted = False
            if self.__volume<Television.MAX_VOLUME:
                self.__volume +=1
    def volume_down(self)->None:
        "this will increase the volume if it aslong as it isnt the min and isnt muted"
        if self.__status:
            self.__muted = False
            if self.__volume>Television.MIN_VOLUME:
                self.__volume -=1
    def __str__(self) ->str:
        "return the status,channel and volume or muted "
        if self.__muted:
            return f'Power = {self.__status} , Channel = {self.__channel} , Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status} , Channel = {self.__channel} , Volume = {self.__volume}'