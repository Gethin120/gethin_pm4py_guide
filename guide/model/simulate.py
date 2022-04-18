"""
对给定的Petri网进行模拟，NO_TRACES决定了生成日志的规模，MAX_TRACE_LENGTH决定了单条迹最大长度。
另外可以指定案例和活动的id，指定时间戳开始时间，详见Parameters。
"""
from pm4py.objects.log.importer.xes.importer import apply as xesimport
from pm4py.algo.discovery.alpha.algorithm import apply as alpha_miner
from pm4py.algo.simulation.playout.petri_net.algorithm import apply as petri_sim
from pm4py.algo.simulation.playout.petri_net.variants.basic_playout import Parameters
from pm4py.statistics.traces.generic.log import case_statistics

log = xesimport('../statics/log/running-example.xes')
net, im, fm = alpha_miner(log)
net_playout = petri_sim(net, im, fm, parameters={Parameters.NO_TRACES: 100, Parameters.MAX_TRACE_LENGTH: 20})
variants_count = case_statistics.get_variant_statistics(net_playout)
print(variants_count)
#todo 使用蒙特卡罗方式模拟Petri网，参考实例