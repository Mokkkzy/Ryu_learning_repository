import array
import array

from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3
from ryu.controller.handler import set_ev_cls
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller import ofp_event
from ryu.lib.packet import packet

'''
实现了数据包的解析功能
'''

class Packetparser(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    
    def __init__(self, *_args, **_kwargs):
        super().__init__(*_args, **_kwargs)
    
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self,ev):
        msg = ev.msg
        
        print('msg.data:',msg.data)
        pkt = packet.Packet(array.array('B',msg.data))
        #protocol
        pName = []
        for p in pkt.protocols:
            print('received protocol data:',p)
            pName.append(p.protocol_name)
            print('src_ip:{0},dst_ip:{1}'.format(p.src_ip,p.dst_ip))
        print('protocol category:',pName)    