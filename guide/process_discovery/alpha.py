"""
alpha算法及其相关算法实现与可视化
"""
from pm4py.objects.log.importer.xes.importer import apply as xes_importer

log = xes_importer('../statics/log/running-example.xes')
# log = xes_importer('../statics/log/receipt.xes')

# 1.使用alpha算法挖掘Petri网
from pm4py.algo.discovery.alpha.algorithm import apply as alpha_miner
net, im, fm = alpha_miner(log)

# 2.可视化
from pm4py.visualization.petri_net import visualizer as pn_vis
# 2.1普通视图
petri_net_alpha = pn_vis.apply(net, im, fm)
pn_vis.view(petri_net_alpha)
# 2.2带有频率属性
parameters = {pn_vis.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
gviz = pn_vis.apply(net, im, fm, parameters=parameters, variant=pn_vis.Variants.FREQUENCY, log=log)
pn_vis.view(gviz)
# 2.3带有间隔时间属性
parameters = {pn_vis.Variants.PERFORMANCE.value.Parameters.FORMAT: "png"}
gviz = pn_vis.apply(net, im, fm, parameters=parameters, variant=pn_vis.Variants.PERFORMANCE, log=log)
pn_vis.view(gviz)

# 3.保存为图片，第二个参数为路径和文件名
# pn_vis.save(gviz,'demo.png')
