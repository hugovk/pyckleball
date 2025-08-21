from datetime import datetime, timedelta
import time
from print_with_color import print_yellow

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        """Start the timer."""
        self.start_time = datetime.now()
        print_yellow(f"Timer started at: {self.start_time.strftime('%m/%d/%y %I:%M:%S %p')}")
        return self  # Return the instance to allow method chaining

    def stop(self):
        """Stop the timer."""
        if self.start_time is None:
            print_yellow("Timer has not been started.")
            return
        self.end_time = datetime.now()
        print_yellow(f"Timer stopped at: {self.end_time.strftime('%m/%d/%y %I:%M:%S %p')}")
        elapsed_time = self.get_elapsed_time()
        print_yellow(f"Elapsed time:               {elapsed_time}")

    def get_elapsed_time(self):
        """Get the elapsed time."""
        if self.start_time is None or self.end_time is None:
            return "Timer has not been started or stopped."
        elapsed = self.end_time - self.start_time
        return str(elapsed)

if __name__ == "__main__":
    timer = Timer().start()
    # Simulate some processing time
    time.sleep(5)
    timer.stop()
