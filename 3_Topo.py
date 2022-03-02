from mininet.topo import Topo


class MyTopo (Topo):
    "ECMP_RR_Test is processing."
    def build (self):
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch5 = self.addSwitch('s5')
        switch6 = self.addSwitch('s6')
    
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        
        
        self.addLink(host1,switch3)
        self.addLink(host2,switch3)
        self.addLink(switch3,switch1)
        self.addLink(switch1,switch5)
        self.addLink(switch1,switch6)
        self.addLink(switch5,switch2)
        self.addLink(switch6,switch2)
        self.addLink(switch2,switch4)
        self.addLink(host3,switch4)
        self.addLink(host4,switch4)
        
topos = {"mytopo":(lambda:MyTopo())}
    
            