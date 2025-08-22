from datetime import datetime, timedelta
import time
from print_with_color import print_yellow

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        """Start the timer when entering the context."""
        self.start_time = datetime.now()
        print_yellow(f"Timer started at:         {self.start_time.strftime('%m/%d/%y %I:%M:%S %p')}")
        return self  # Return the instance for use inside the context

    def __exit__(self, exc_type, exc_value, traceback):
        """Stop the timer when exiting the context."""
        if self.start_time is None:
            print_yellow("Timer has not been started.")
            return
        self.end_time = datetime.now()
        print_yellow(f"Timer stopped at:         {self.end_time.strftime('%m/%d/%y %I:%M:%S %p')}")
        self.get_elapsed_time(self.end_time)

    def split(self):
        """Get the current split time without stopping the timer."""
        if self.start_time is None:
            print_yellow("Timer has not been started.")
            return
        current_time = datetime.now()
        print_yellow(f"Timer split check:        {current_time.strftime('%m/%d/%y %I:%M:%S %p')}")
        self.get_elapsed_time(current_time)

    def get_elapsed_time(self, elapsed_time_moment):
        """Get the elapsed time."""
        if self.start_time is None:
            return "Timer has not been started or stopped."
        elapsed = elapsed_time_moment - self.start_time
        print_yellow(f"Timer total elapsed time:           {elapsed}")
        # return str(elapsed)

if __name__ == "__main__":
    # timer = Timer()
    # time.sleep(3)
    # timer.stop()

    with Timer() as timer:
        # Simulate some processing time
        time.sleep(2)
        timer.split()
        time.sleep(3)
        # Simulate an error
        raise Exception("An error occurred during processing!")
        # timer.stop()
