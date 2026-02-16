import unittest


from television_OOP.Television import Television





class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.television = Television()

    def test_that_television_initial_state_is_off(self):
        expected_initial_state = "off"
        actual_initial_state = self.television.get_status()
        self.assertEqual(expected_initial_state , actual_initial_state)

    def test_that_television_can_be_turn_on(self):
        self.assertEqual("off" , self.television.get_status())
        turn_TV_on = self.television.turn_tv_on()
        self.assertEqual("on", self.television.get_status())

    def test_that_television_can_be_turn_off(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        self.television.turn_tv_off()
        self.assertEqual("off", self.television.get_status())

    def test_that_volume_initial_state_is_0(self):
        expected_initial_state = 0
        actual_initial_state = self.television.get_volume_state()
        self.assertEqual(expected_initial_state, actual_initial_state)

    # def test_that_volume_can_be_increase(self):
    #     self.assertEqual(0, self.television.get_volume_state())
    #     self.television.increase_volume()
    #     self.assertEqual(1, self.television.get_volume_state())

    def test_that_volume_can_only_be_increase_when_tv_is_on(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        self.television.increase_volume()
        self.assertEqual(1, self.television.get_volume_state())

    def test_that_volume_cannot_be_increase_when_tv_is_off(self):
        self.assertEqual("off", self.television.get_status())
        # self.television.increase_volume()
        with self.assertRaises(Exception):
            self.television.increase_volume()

    def test_that_volume_can_only_be_decrease_when_volume_is_increased(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        self.television.increase_volume()
        self.television.increase_volume()
        self.television.increase_volume()
        self.assertEqual(3, self.television.get_volume_state())
        self.television.decrease_volume()
        self.assertEqual(2, self.television.get_volume_state())

    def test_that_volume_cannot_be_increase_when_volume_is_10(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        self.television.increase_volume()
        self.television.increase_volume()
        self.television.increase_volume()
        self.television.increase_volume()
        self.television.increase_volume()
        self.television.increase_volume()
        self.television.increase_volume()
        self.television.increase_volume()
        self.television.increase_volume()
        self.television.increase_volume()
        with self.assertRaises(Exception):
            self.television.increase_volume()


    def test_that_volume_cannot_be_decrease_when_tv_off(self):
        self.assertEqual("off", self.television.get_status())
        with self.assertRaises(Exception):
            self.television.decrease_volume()

    def test_that_volume_cannot_be_decrease_when_volume_is_0(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        with self.assertRaises(Exception):
            self.television.decrease_volume()

    def test_the_initial_state_of_channel(self):
        self.assertEqual(1, self.television.get_channel_state())


    def test_that_you_can_switch_chanel_by_increasing(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        self.television.change_channel_by_increasing()
        self.assertEqual(2, self.television.get_channel_state())

    def test_that_you_cannot_switch_tv_if_Tv_is_off(self):
        self.assertEqual("off", self.television.get_status())
        with self.assertRaises(Exception):
            self.television.change_channel_by_increasing()


    def test_that_you_cannot_exceed_the_max_channel(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        with self.assertRaises(Exception):
            self.television.change_channel_by_increasing()

    def test_that_you_can_change_channel_by_decreasing(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_increasing()
        self.television.change_channel_by_decreasing()
        self.assertEqual(3, self.television.get_channel_state())

    def test_that_you_cannot_change_channel_by_decreasing_when_tv_is_off(self):
        self.assertEqual("off", self.television.get_status())
        with self.assertRaises(Exception):
            self.television.change_channel_by_decreasing()

    def test_that_you_cannot_change_channel_when_channel_is_1(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        with self.assertRaises(Exception):
            self.television.change_channel_by_decreasing()


    def test_that_you_can_change_channel_by_inputing_channel_number(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        self.television.change_channel_by_inputing_channel_number(8)
        self.assertEqual(8, self.television.get_channel_state())

    def test_that_you_cannot_change_channel_by_inputing_channel_number_when_tv_is_off(self):
        self.assertEqual("off", self.television.get_status())
        with self.assertRaises(Exception):
            self.television.change_channel_by_inputing_channel_number(8)

    def test_that_you_cannot_change_channel_by_inputing_channel_number_that_exceed_10(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        with self.assertRaises(Exception):
            self.television.change_channel_by_inputing_channel_number(14)

    def test_that_you_cannot_change_channel_by_inputing_channel_number_that_is_below_1(self):
        self.assertEqual("off", self.television.get_status())
        self.television.turn_tv_on()
        with self.assertRaises(Exception):
            self.television.change_channel_by_inputing_channel_number(0)

if __name__ == '__main__':
    unittest.main()
