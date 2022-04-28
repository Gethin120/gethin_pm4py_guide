import pm4py
from pm4py.objects.log.importer.xes.importer import apply as xes_importer


def time_info(log):
    #
    from pm4py.statistics.sojourn_time.log.get import apply

    from pm4py.statistics.traces.cycle_time.log.get import apply

    from pm4py.statistics.passed_time.log.algorithm import apply
    # 案例持续时间
    from pm4py.statistics.traces.generic.log import case_statistics
    cases = case_statistics.get_cases_description(log, parameters={
        case_statistics.Parameters.TIMESTAMP_KEY: "time:timestamp"})
    all_case_durations = [x["caseDuration"] for x in cases.values()]
    print("案例持续时间", all_case_durations)
    # 案例持续时间中位数
    from pm4py.statistics.traces.generic.log import case_statistics
    median_case_duration = case_statistics.get_median_case_duration(log, parameters={
        case_statistics.Parameters.TIMESTAMP_KEY: "time:timestamp"
    })
    print("案例持续时间分布中位数", median_case_duration)

    from pm4py.statistics.traces.generic.log import case_arrival
    case_arrival_ratio = case_arrival.get_case_arrival_avg(log, parameters={
        case_arrival.Parameters.TIMESTAMP_KEY: "time:timestamp"})
    from pm4py.statistics.traces.generic.log import case_arrival
    case_dispersion_ratio = case_arrival.get_case_dispersion_avg(log, parameters={
        case_arrival.Parameters.TIMESTAMP_KEY: "time:timestamp"})
    print(case_arrival_ratio, case_dispersion_ratio)


if __name__ == '__main__':
    # log = xes_importer('../statics/log/running-example.xes')
    log = xes_importer('../statics/log/receipt.xes')

    time_info(log)
    # todo
    # print(get_events_distribution(log))
