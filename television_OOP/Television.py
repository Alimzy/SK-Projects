class Television:
    status = "off"
    volume = 0
    channel = 1

    def get_status(self):
        return self.status

    def turn_tv_off(self):
        self.status = "off"

    def turn_tv_on(self):
        self.status = "on"

    def get_volume_state(self):
        return self.volume

    def increase_volume(self):
        if self.status == "off":
            raise Exception("TV is off you cannot increase volume")
        if self.volume == 10:
            raise Exception("This is the maximum volume")
        self.volume+=1

    def decrease_volume(self):
        if self.status == "off":
            raise Exception("TV is off you cannot decrease volume")
        if self.volume == 0:
            raise Exception("This is the minimum volume")
        self.volume -= 1

    def get_channel_state(self):
        return self.channel

    def change_channel_by_increasing(self):
        if self.status == "off":
            raise Exception("TV is off you cannot change channel")
        if self.channel == 10:
            raise Exception("This is the maximum channel")
        self.channel+=1

    def change_channel_by_decreasing(self):
        if self.status == "off":
            raise Exception("TV is off you cannot change channel")
        if self.channel == 1:
            raise Exception("This is the minimum channel")
        self.channel-=1

    def change_channel_by_inputing_channel_number(self, myChannelNumber):
        if self.status == "off":
            raise Exception("TV is off you cannot change channel")
        if myChannelNumber > 10:
            raise Exception("Channel does not exist")
        if myChannelNumber < 1:
            raise Exception("Channel does not exist")
        self.channel = myChannelNumber




