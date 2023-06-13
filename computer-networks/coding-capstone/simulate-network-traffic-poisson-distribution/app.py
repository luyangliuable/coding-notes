# This app predicts the likelihood of a certain number of traffic arriving

import random as rand
import time
import math

def simulate(k, possible_range):
    """
    Simulates the arrival of packets to a server
    """

    all_packets = []

    if not isinstance(k, int) or k < 0:
        print("The number of events 'k' must be a non-negative integer.")
        return

    print("Start simlation...")
    while 1:
        # Number of traffic coming in this second
        new_packets = rand.randint(0, possible_range)

        all_packets += [ new_packets ]

        # Average amount of network coming in per second
        if (len(all_packets) > 0):
            l = sum(all_packets) / len(all_packets)
        else:
            l = sum(all_packets) / 1

        # l = 100

        print("New packets: {}, average number of packets: {}".format(new_packets, l))

        # Poisson distribution
        # P(k) = (lambda^k * e^-lambda) / k

        P = 0

        for i in range(k+1):
            P += (l**i * math.exp(-l)) / math.factorial(i)

        print("The likelihood of less than {} packets arriving in the next second is {}".format(k, P))
        time.sleep(1)

simulate(100, 1000)


# References:
# https://www.cse.iitb.ac.in/~br/webpage/courses/cs625-fall2003/lec-notes/lec-notes28-1.html#:~:text=Poisson%20distribution%20is%20often%20used,(independent%20identically%20distributed)%20process.
