import threading
from time import sleep
import os


numPhilosophers = 4
philosophers = []
forks = []


class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

    def run(self):
        left_fork_index = self.index
        right_fork_index = (self.index - 1) % numPhilosophers
        fork_pair = ForkPair(left_fork_index, right_fork_index)
        while True:
            fork_pair.pickUp()
            print("Philosopher", self.index, "eats.")
            fork_pair.putDown()

class ForkPair:
    def __init__(self, left_fork_index, right_fork_index):
        if left_fork_index > right_fork_index:
            left_fork_index, right_fork_index = right_fork_index, left_fork_index
        self.first_fork = forks[left_fork_index]
        self.second_fork = forks[right_fork_index]

    def pickUp(self):
        self.first_fork.acquire()
        self.second_fork.acquire()

    def putDown(self):
        self.first_fork.release()44
        self.second_fork.release()


if __name__ == "__main__":
    for i in range(0, numPhilosophers):
        philosophers.append(Philosopher(i))
        forks.append(threading.Lock())

    for philosopher in philosophers:
        philosopher.start()

    try:
        while True: sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)