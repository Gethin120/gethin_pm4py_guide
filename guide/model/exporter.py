from pm4py.objects.petri_net.exporter.exporter import apply as pn_exporter
from pm4py.objects.petri_net.importer.importer import apply as pnml_importer
from pm4py.objects.petri_net.importer.importer import Variants

net, im, fm = pnml_importer('../statics/model/running-example.pnml', variant=Variants.PNML)
pn_exporter(net, initial_marking=im, final_marking=fm,output_filename='example.pnml')
