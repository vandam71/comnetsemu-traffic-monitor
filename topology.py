from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

import random

class SimpleTopology:
    def __init__(self):
        self.net = Mininet(controller=RemoteController)

        # Adding a remote controller
        self.c0 = self.net.addController(name='c0', controller=RemoteController, ip='127.0.0.1', port=6633)

        # Adding switches and hosts
        self.s1 = self.net.addSwitch('s1')
        self.s2 = self.net.addSwitch('s2')

        self.h1 = self.net.addHost('h1', ip='10.0.0.1/24')
        self.h2 = self.net.addHost('h2', ip='10.0.0.2/24')
        self.h3 = self.net.addHost('h3', ip='10.0.0.3/24')
        self.h4 = self.net.addHost('h4', ip='10.0.0.4/24')
        self.h5 = self.net.addHost('h5', ip='10.0.0.5/24')

        # Adding links between hosts and switches
        self.net.addLink(self.h1, self.s1)
        self.net.addLink(self.h2, self.s1)
        self.net.addLink(self.h3, self.s1)
        self.net.addLink(self.h4, self.s2)
        self.net.addLink(self.h5, self.s2)

        # Adding links between switches
        self.net.addLink(self.s1, self.s2)

    def start(self):
        self.net.start()

        # Generating random traffic
        self.generate_random_traffic()

        # Starting Mininet CLI for interactive testing
        CLI(self.net)

    def stop(self):
        self.net.stop()

    def generate_random_traffic(self):
        # Generate random traffic between random pairs of hosts
        num_pairs = 50  # Number of random pairs

        for _ in range(num_pairs):
            host1, host2 = random.sample(self.net.hosts, 2)
            info(f"Generating random traffic between {host1.name} and {host2.name}\n")
            host1.cmd(f"ping -c 100 {host2.IP()} &")  # Example: Ping between hosts
            # You can also use iperf or other tools for generating different types of traffic

if __name__ == '__main__':
    setLogLevel('info')
    topology = SimpleTopology()
    topology.start()
    topology.stop()
