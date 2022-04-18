"""
导入Petri网模型，输入格式一般为pnml(petri net ml)
"""

from pm4py.objects.petri_net.importer.importer import apply as pnml_importer
from pm4py.objects.petri_net.importer.importer import Variants
from pm4py.visualization.petri_net import visualizer as pn_vis

net, im, fm = pnml_importer('../statics/model/running-example.pnml', variant=Variants.PNML)
petri_net_alpha = pn_vis.apply(net, im, fm)
pn_vis.view(petri_net_alpha)
