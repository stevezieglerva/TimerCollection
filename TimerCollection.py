import time
from collections import OrderedDict



class TimerCollection():
	def __init__(self):
		self.timers = OrderedDict()
		self.__timer_starts = {}


	def start_timer(self, name):
		self.__timer_starts[name] = time.time()


	def end_timer(self, name):
		end = time.time()
		if name in self.__timer_starts:
			start = self.__timer_starts[name]
			elapsed = int(end - start)
			if name in self.timers:
				self.timers[name] = self.timers[name] + elapsed
			else:
				self.timers[name] = elapsed

	
	def print_results(self):
		print(self.timers)

	def __str__(self):
		str(self.timers)
	
