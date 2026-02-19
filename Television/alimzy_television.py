class AlimzyTelevision:
    __MINIMUM_VOLUME = 0
    __MAXIMUM_VOLUME = 100
    __MAXIMUM_CHANNELS = 100
    __MINIMUM_CHANNELS = 1

    def __init__(self):
        self.__status = False
        self.__volume = 0
        self.__channel = 1

    def get_status(self):
        return self.__status

    def turn_tv_on(self):
        self.__status = True

    def turn_tv_off(self):
        self.__status = False

    def get_volume(self):
        return self.__volume

    def increase_tv_volume(self):
        if not self.__status:
            raise ValueError("Tv is off, you cannot increase the volume")
        if self.__volume == self.MAXIMUM_VOLUME:
            raise ValueError("This is the maximum value, you cannot exceed this")
        self.__volume += 1

    def decrease_tv_volume(self):
        if not self.__status:
            raise ValueError("Tv is off, you cannot turn on Tv")
        if self.__volume == self.MINIMUM_VOLUME:
            raise ValueError("This is the minimum volume of Tv, you cannot exceed this")
        self.__volume -= 1



    def change_channel_by_increasing(self):
        if not self.__status:
            raise ValueError("You cannot change channel, TV is off")
        if self.__channel == self.MAXIMUM_CHANNELS:
            raise ValueError("This is the minimum channel of Tv, you cannot exceed this")
        self.__channel +=1

    def get_channel(self):
        return self.__channel

    def change_channel_by_decreasing(self):
        if not self.__status:
            raise ValueError("Tv is off, you cannot turn on Tv")
        if self.__channel == self.MINIMUM_CHANNELS:
            raise ValueError("This is the minimum channel of Tv, you cannot exceed this")
        self.__channel -= 1

    def change_channel_by_inputing_value(self,input_value):
        if not self.__status:
            raise ValueError("Tv is off, you cannot turn on Tv")
        if input_value > 100:
            raise ValueError("Tv is off, you cannot turn on Tv")
        if input_value < 0:
            raise ValueError("Tv is off, you cannot turn on Tv")
        self.__channel = input_value




