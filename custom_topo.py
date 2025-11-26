# custom_topo.py
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import RemoteController

class CustomTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)

def main():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=RemoteController)
    net.addController('c0')
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    main()
