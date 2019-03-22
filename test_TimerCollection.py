import unittest
from TimerCollection import *

class TestTimerCollection(unittest.TestCase):
	def test_constructor__created(self):
		# Arrange


		# Act
		subject = TimerCollection()

		# Assert
		self.assertEqual(len(subject.timers), 0)

		return 1


	def test_constructor__end_timer__timers_has_elapsed_time(self):
		# Arrange
		subject = TimerCollection()
		subject.start_timer("timer 1")

		# Act
		time.sleep(1)
		subject.end_timer("timer 1")
		print(subject.timers)

		# Assert
		self.assertGreater(subject.timers["timer 1"], .9)


	def test_constructor__time_twice__timers_has_elapsed_time(self):
		# Arrange
		subject = TimerCollection()
		subject.start_timer("timer 10")
		time.sleep(1)
		subject.end_timer("timer 10")


		# Act
		subject.start_timer("timer 10")
		time.sleep(2)
		subject.end_timer("timer 10")
		print(subject.timers)
		# Assert
		self.assertGreater(subject.timers["timer 10"], 2)


	def test_constructor__two_separate_timers__timers_has_elapsed_time(self):
		# Arrange
		subject = TimerCollection()

		# Act
		subject.start_timer("timer A")
		time.sleep(1)
		subject.start_timer("timer B")
		time.sleep(1)
		subject.end_timer("timer B")
		subject.start_timer("timer C")
		subject.end_timer("timer C")
		time.sleep(2)
		subject.end_timer("timer A")
		print(subject.timers)

		# Assert
		self.assertGreater(subject.timers["timer A"], 3)
		self.assertGreater(subject.timers["timer A"], 1)



if __name__ == '__main__':
	unittest.main()		


