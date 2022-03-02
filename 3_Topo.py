from mininet.topo import Topo


class MyTopo (Topo):
    "ECMP_RR_Test is processing."
    def build (self):
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        node3 = self.addNode('n3')
        node4 = self.addNode('n4')
        node5 = self.addNode('n5')
        node6 = self.addNode('n6')
        
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        
        
        self.addLink(host1,node3)
        self.addLink(host2,node3)
        self.addLink(node3,switch1)
        self.addLink(switch1,node5)
        self.addLink(switch1,node6)
        self.addLink(node5,switch2)
        self.addLink(node6,switch2)
        self.addLink(switch2,node4)
        self.addLink(host3,node4)
        self.addLink(host4,node4)
        
topos = {"mytopo":(lambda:MyTopo())}
    
            