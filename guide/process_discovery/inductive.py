"""
inductive算法及其相关算法实现与可视化
"""
from pm4py.objects.log.importer.xes.importer import apply as xes_importer


def IM_alpha(log):
    # 使用inductive算法挖掘Petri网
    from pm4py.algo.discovery.inductive import algorithm as inductive_miner
    net, im, fm = inductive_miner.apply(log)
    # 可视化
    from pm4py.visualization.petri_net import visualizer as pn_vis
    petri_net_alpha = pn_vis.apply(net, im, fm)
    pn_vis.view(petri_net_alpha)


def IM_process_tree(log):
    # 使用inductive算法挖掘进程树
    from pm4py.algo.discovery.inductive import algorithm as inductive_miner
    tree = inductive_miner.apply_tree(log)
    # 进程树可视化
    from pm4py.visualization.process_tree import visualizer as pt_visualizer
    gviz = pt_visualizer.apply(tree)
    pt_visualizer.view(gviz)


def IM_f(log):
    # inductive miner frequent
    from pm4py.algo.discovery.inductive import algorithm as inductive_miner
    net, im, fm = inductive_miner.apply(log, variant=inductive_miner.IMf)
    # 可视化
    from pm4py.visualization.petri_net import visualizer as pn_vis
    petri_net_alpha = pn_vis.apply(net, im, fm)
    pn_vis.view(petri_net_alpha)

def IM_d(log):
    # inductive miner dfg
    from pm4py.algo.discovery.inductive import algorithm as inductive_miner
    net, im, fm = inductive_miner.apply(log, variant=inductive_miner.IMd)
    # 可视化
    from pm4py.visualization.petri_net import visualizer as pn_vis
    petri_net_alpha = pn_vis.apply(net, im, fm)
    pn_vis.view(petri_net_alpha)

def IM_clean(log):
    # inductive miner
    #TODO
    from pm4py.algo.discovery.inductive import algorithm as inductive_miner
    net, im, fm = inductive_miner.apply(log, variant=inductive_miner.IM_CLEAN)
    # 可视化
    from pm4py.visualization.petri_net import visualizer as pn_vis
    petri_net_alpha = pn_vis.apply(net, im, fm)
    pn_vis.view(petri_net_alpha)

if __name__ == '__main__':
    log = xes_importer('../statics/log/running-example.xes')
    # log = xes_importer('../statics/log/receipt.xes')
    # IM_alpha(log)
    # IM_process_tree(log)
    # IM_f(log)
    # IM_d(log)
    # IM_clean(log)
