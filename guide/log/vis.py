from pm4py.objects.log.importer.xes.importer import apply as xes_importer
log = xes_importer('../statics/log/running-example.xes')

# from pm4py.statistics.eventually_follows.log import get as efg_get
#
# efg_graph = efg_get.apply(log)
# print(efg_graph)

from pm4py.algo.filtering.log.attributes import attributes_filter

x, y = attributes_filter.get_kde_numeric_attribute(log, "amount")

from pm4py.visualization.graphs import visualizer as graphs_visualizer

gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.ATTRIBUTES)
graphs_visualizer.view(gviz)

from pm4py.visualization.graphs import visualizer as graphs_visualizer

gviz = graphs_visualizer.apply_semilogx(x, y, variant=graphs_visualizer.Variants.ATTRIBUTES)
graphs_visualizer.view(gviz)