"""
检查Petri网的性质

1.检查Petri网是否是工作流网
    唯一源库所
    唯一目标库所
    每个节点都在源库所到目标库所路径上
2.工作流网是否健壮sound
    不包含活锁
    不包含死锁
    可以到的最终标记

"""

from pm4py.objects.petri_net.importer.importer import apply as pnml_importer
net, im, fm = pnml_importer('../statics/model/running-example.pnml', variant=Variants.PNML)

from pm4py.algo.analysis.workflow_net import algorithm
algorithm.apply(net)

from pm4py.algo.analysis.woflan import algorithm as woflan
woflan.apply(net, im, fm)
