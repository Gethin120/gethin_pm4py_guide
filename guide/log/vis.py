import pm4py
from pm4py.objects.log.importer.xes.importer import apply as xes_importer

# from pm4py.statistics.eventually_follows.log import get as efg_get
#
# efg_graph = efg_get.apply(log)
# print(efg_graph)

# from pm4py.algo.filtering.log.attributes import attributes_filter
#
# x, y = attributes_filter.get_kde_numeric_attribute(log, "amount")
#
# from pm4py.visualization.graphs import visualizer as graphs_visualizer
#
# gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.ATTRIBUTES)
# graphs_visualizer.view(gviz)
#
# from pm4py.visualization.graphs import visualizer as graphs_visualizer
#
# gviz = graphs_visualizer.apply_semilogx(x, y, variant=graphs_visualizer.Variants.ATTRIBUTES)
# graphs_visualizer.view(gviz)


# 性能谱，时间为横坐标，活动为纵坐标，展示活动之间的转移关系

# pm4py.view_performance_spectrum(log, ["Confirmation of receipt", "T04 Determine confirmation of receipt",
#                                       "T10 Determine necessity to stop indication"], format="svg")

# log = xes_importer('../statics/log/running-example.xes')
# pm4py.view_performance_spectrum(log, ['register request', 'check ticket', 'pay compensation'], format='svg')
import os


def display_graph(log):
    from pm4py.util import constants
    from pm4py.statistics.traces.generic.log import case_statistics
    x, y = case_statistics.get_kde_caseduration(log, parameters={
        constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "time:timestamp"})

    from pm4py.visualization.graphs import visualizer as graphs_visualizer

    gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.CASES)
    # graphs_visualizer.view(gviz)

    gviz = graphs_visualizer.apply_semilogx(x, y, variant=graphs_visualizer.Variants.CASES)
    # graphs_visualizer.view(gviz)

    from pm4py.algo.filtering.log.attributes import attributes_filter

    x, y = attributes_filter.get_kde_date_attribute(log, attribute="time:timestamp")

    from pm4py.visualization.graphs import visualizer as graphs_visualizer

    gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.DATES)
    # graphs_visualizer.view(gviz)

    import os
    from pm4py.objects.log.importer.xes import importer as xes_importer

    log = xes_importer.apply('../statics/log/roadtraffic100traces.xes')

    from pm4py.algo.filtering.log.attributes import attributes_filter

    x, y = attributes_filter.get_kde_numeric_attribute(log, "amount")

    from pm4py.visualization.graphs import visualizer as graphs_visualizer

    gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.ATTRIBUTES)
    graphs_visualizer.view(gviz)

    from pm4py.visualization.graphs import visualizer as graphs_visualizer

    gviz = graphs_visualizer.apply_semilogx(x, y, variant=graphs_visualizer.Variants.ATTRIBUTES)
    graphs_visualizer.view(gviz)


def dotted_chart(log):
    # 没有指定属性参数的时候，默认x轴时间，y轴案例，不同颜色标识的活动
    # 最多三个属性参数，x轴y轴和颜色属性。例如可以区分不同组织和组织里的成员
    pm4py.view_dotted_chart(log, format="svg")
    pm4py.view_dotted_chart(log, format="svg", attributes=["concept:name", "org:resource", "Resource"])


def event_time_distr(log):
    # 绘制不同时间单位下的活动分布图
    # distr_type可选hours,days_week,days_month,months,years.
    pm4py.view_events_distribution_graph(log, distr_type="days_week", format="svg")


if __name__ == '__main__':
    log = xes_importer('../statics/log/running-example.xes')
    # log = xes_importer('../statics/log/receipt.xes')
    # dotted_chart(log)
    event_time_distr(log)
