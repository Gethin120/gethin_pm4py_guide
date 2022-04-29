"""
alpha算法及其相关算法实现与可视化
"""
from pm4py.objects.log.importer.xes.importer import apply as xes_importer

log = xes_importer('../statics/log/running-example.xes')
# log = xes_importer('../statics/log/receipt.xes')

# 使用alpha算法挖掘Petri网
from pm4py.algo.discovery.alpha.algorithm import apply as alpha_miner
net, im, fm = alpha_miner(log)

# 可视化
from pm4py.visualization.petri_net import visualizer as pn_vis
petri_net_alpha = pn_vis.apply(net, im, fm)
pn_vis.view(petri_net_alpha)
# petri_net_alpha = pn_vis.apply(net, im, fm, variant=pn_vis.Variants.PERFORMANCE,)
# pn_vis.view(petri_net_alpha)
# petri_net_alpha = pn_vis.apply(net, im, fm, variant=pn_vis.FREQUENCY_DECORATION)
# pn_vis.view(petri_net_alpha)
