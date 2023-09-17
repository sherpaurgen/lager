import gevent
from gevent import monkey

# Monkey-patch the standard library to make it gevent-friendly (optional but recommended)
monkey.patch_all()

# Function to simulate a non-blocking task
def task(name, delay):
    gevent.sleep(delay)
    print(f"Task {name} is complete")

# Create greenlets for three tasks with different delays
greenlet1 = gevent.spawn(task, "A", 1)
greenlet2 = gevent.spawn(task, "B", 2)
greenlet3 = gevent.spawn(task, "C", 13)

# Wait for all greenlets to finish
gevent.joinall([greenlet1, greenlet2, greenlet3])