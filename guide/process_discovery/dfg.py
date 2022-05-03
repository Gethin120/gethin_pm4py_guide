"""
dfg直接跟随流图
"""
from pm4py.objects.log.importer.xes.importer import apply as xes_importer

log = xes_importer('../statics/log/running-example.xes')
# log = xes_importer('../statics/log/receipt.xes')

# 1.使用dfg算法挖掘直接跟随流图
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery

dfg = dfg_discovery.apply(log)

# 2.可视化
# 2.1带频率视图
from pm4py.visualization.dfg import visualizer as dfg_visualization

gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.FREQUENCY)
dfg_visualization.view(gviz)

# 2.2带时间间隔视图
from pm4py.visualization.dfg import visualizer as dfg_visualization

gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.PERFORMANCE)
dfg_visualization.view(gviz)
