from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls


class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    
    def __init__(self, *_args, **_kwargs):
        super().__init__(*_args, **_kwargs)
    
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self,ev):
        msg = ev.msg
        dp = msg.datapath
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser
        dp_id = dp.id
        
        # 计算出in_port
        start = str(msg).index('oxm_fields') + 11
        end = str(msg).index('),reason')
        inport_str = str(msg)[start:end]
        instr = eval(inport_str)
        in_port = instr['in_port']
        
        actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]
        
        data = None
        if msg.buffer_id == ofp.OFP_NO_BUFFER:
            data = msg.data
        print('id:{0}'.format(dp_id))
        print('in_port:{0}'.format(in_port))
        
        out = ofp_parser.OFPPacketOut(
            datapath = dp, buffer_id = msg.buff_id, in_port = in_port,
            actions = actions,data = data
        )
        dp.send_msg(out)
"""
官方版本 執行不了 AttributeError: PacketIn沒有“In_port"
from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls


# 继承app_manager
class L2switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION] # 导入openflow_v1.3协议的数据
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self,ev):
        msg = ev.msg
        dp = msg.datapath
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser
        
        actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]
        
        data = None
        if msg.buffer_id == ofp.OFP_NO_BUFFER:
            data = msg.data
        
        out = ofp_parser.OFPPacketOut(
            datapath = dp, buffer_id = msg.buffer_id, in_port = msg.in_port,
            actions = actions, data = data
        )
        dp.send_msg(out)
"""

