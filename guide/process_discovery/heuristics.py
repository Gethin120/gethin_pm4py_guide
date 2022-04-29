"""
启发式网
"""
from pm4py.objects.log.importer.xes.importer import apply as xes_importer


def heuristics_miner(log):
    # 启发式挖掘Petri网，阈值设置为0.99
    from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
    net, im, fm = heuristics_miner.apply(log, parameters={
        heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.99})

    from pm4py.visualization.petri_net import visualizer as pn_visualizer
    gviz = pn_visualizer.apply(net, im, fm)
    pn_visualizer.view(gviz)


def heuristics_miner_hn(log):
    # 启发式算法挖掘启发网，可以转化成Petrinet，暂时未找到保存为.hn的方式。
    from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
    heu_net = heuristics_miner.apply_heu(log, parameters={
        heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.99})
    from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
    gviz = hn_visualizer.apply(heu_net)
    hn_visualizer.view(gviz)


def heuristics_miner_plusplus(log):
    # 启发式++算法挖掘Petri网
    from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
    net, im, fm = heuristics_miner.apply(log, parameters={
        heuristics_miner.Variants.PLUSPLUS.value.Parameters.DEPENDENCY_THRESH: 0.99})

    from pm4py.visualization.petri_net import visualizer as pn_visualizer
    gviz = pn_visualizer.apply(net, im, fm)
    pn_visualizer.view(gviz)


if __name__ == '__main__':
    # log = xes_importer('../statics/log/running-example.xes')
    log = xes_importer('../statics/log/receipt.xes')
    # heuristics_miner(log)
    # heuristics_miner_hn(log)
    heuristics_miner_plusplus(log)
