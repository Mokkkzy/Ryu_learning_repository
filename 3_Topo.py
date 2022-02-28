import imp
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class ECMP_round_request(Topo):
    "ECMP_RR_Test is processing."
    def __init__(self):
        switch = []
        host = []
        for s in range(6):
            switch[s+1] = self.addSwitch('s%s'%(s+1))
        
        for h in range(4):
            host[h+1] = self.addHost('h%h'%(h+1))
        
        self.addLink(host[1],switch[3])
        self.addLink(host[2],switch[3])
        self.addLink(switch[3],switch[1])
        self.addLink(switch[1],switch[5])
        self.addLink(switch[1],switch[6])
        self.addLink(switch[5],switch[2])
        self.addLink(switch[6],switch[2])
        self.addLink(host[3],switch[2])
        self.addLink(host[4],switch[2])
        
topos = {"mytopo":(lambda:ECMP_round_request())}
    
            