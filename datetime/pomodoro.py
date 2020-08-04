from datetime import datetime, timedelta, time
import time as timer
# todo: flask, test, custom interval
class PomodoroWatch:
    def __init__(self):
        self.interval = time(0, 1, 0)
        self.is_running = False
        self.current = time(0, 1, 0)

    def start(self):
        """ Starts/resumes stopwatch """
        if not self.is_running:
            while self.current != time(0, 0, 0):
                delta = timedelta(seconds=1)
                self.current = (datetime.combine(datetime.today(),self.current) - delta).time()
                print(self.current)
                timer.sleep(1)
      
    def pause(self):
        """ Pause stopwatch """
        self.is_running = False
        print('Pomodoro is paused')

    def reset(self):
        """ Resets stopwatch to initial interval value """
        self.current = self.interval
        self.is_running = False
        print('Pomodoro is reset')
    


if __name__ == '__main__':
    pomodoro = PomodoroWatch()
    pomodoro.start()
