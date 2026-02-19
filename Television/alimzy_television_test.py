import unittest

from alimzy_television import AlimzyTelevision



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.television_one = AlimzyTelevision()

    def test_that_television_initial_status_is_off(self):
        self.assertFalse(self.television_one.get_status())

    def test_that_television_can_be_turn_on(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        self.assertTrue( self.television_one.get_status())


    def test_that_television_can_be_turn_off_after_it_has_been_on(self):
        self.assertFalse( self.television_one.get_status())
        self.television_one.turn_tv_on()
        self.television_one.turn_tv_off()
        self.assertFalse( self.television_one.get_status())


    def test_that_volume_initial_status_is_zero(self):
        self.assertFalse(self.television_one.get_status())
        self.assertEqual(0, self.television_one.get_volume())

    def test_that_volume_can_increase_when_tv_is_on(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        self.television_one.increase_tv_volume()
        self.assertEqual(1, self.television_one.get_volume())

    def test_that_volume_cannot_be_increase_when_tv_is_off(self):
        self.assertFalse(self.television_one.get_status())
        with self.assertRaises(ValueError):
            self.television_one.increase_tv_volume()

    def test_that_decrease_volume_button_is_working_when_tv_is_on(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        self.television_one.increase_tv_volume()
        self.television_one.increase_tv_volume()
        self.television_one.decrease_tv_volume()
        self.assertEqual(1, self.television_one.get_volume())


    def test_that_volume_cannot_be_decrease_when_tv_is_off(self):
        self.assertFalse(self.television_one.get_status())
        with self.assertRaises(ValueError):
            self.television_one.decrease_tv_volume()

    def test_that_you_cannot_decrease_volume_when_volume_is_zero(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        with self.assertRaises(ValueError):
            self.television_one.decrease_tv_volume()

    def test_that_volume_cannot_exceed_the_maximum_value(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        for count in range(0,100):
            self.television_one.increase_tv_volume()
        with self.assertRaises(ValueError):
            self.television_one.increase_tv_volume()

    def test_that_change_channel_button_by_increasing_is_working_when_tv_is_on(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        self.television_one.change_channel_by_increasing()
        self.assertEqual(2,self.television_one.get_channel())

    def test_that_change_channel_button_by_increasing_is_not_working_when_tv_is_off(self):
        self.assertFalse(self.television_one.get_status())
        with self.assertRaises(ValueError):
            self.television_one.change_channel_by_increasing()

    def test_that_change_channel_button_by_increasing_cannot_exceed_the_maximum_channel(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        for count in range(1,100):
            self.television_one.change_channel_by_increasing()
        with self.assertRaises(ValueError):
            self.television_one.change_channel_by_increasing()

    def test_that_change_channel_button_by_decreasing_is_working_when_tv_is_on(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        self.television_one.change_channel_by_increasing()
        self.television_one.change_channel_by_decreasing()
        self.assertEqual(1, self.television_one.get_channel())

    def test_that_change_channel_button_by_decreasing_is_not_working_when_tv_is_off(self):
        self.assertFalse(self.television_one.get_status())
        with self.assertRaises(ValueError):
            self.television_one.change_channel_by_decreasing()

    def test_that_change_channel_button_by_decreasing_cannot_exceed_the_minimum_value(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        with self.assertRaises(ValueError):
            self.television_one.change_channel_by_decreasing()


    def test_that_change_channel_button_by_inputing_value_is_working_when_tv_is_on(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        self.television_one.change_channel_by_inputing_value(56)
        self.assertEqual(56, self.television_one.get_channel())

    def test_that_change_channel_button_by_inputing_value_is_not_working_when_tv_is_off(self):
        self.assertFalse(self.television_one.get_status())
        with self.assertRaises(ValueError):
            self.television_one.change_channel_by_inputing_value(67)

    def test_that_change_channel_button_by_inputing_value_cannot_exceed_the_maximum_value(self):
        self.assertFalse(self.television_one.get_status())
        self.television_one.turn_tv_on()
        with self.assertRaises(ValueError):
            self.television_one.change_channel_by_inputing_value(120)

   