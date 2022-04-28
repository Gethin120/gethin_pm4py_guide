import pm4py
from pm4py.objects.log.importer.xes.importer import apply as xes_importer


def time_info(log):
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

    # 逗留时间，实验了几个日志都为0，猜测是需要事件生命周期属性<string key="lifecycle:transition" value="In Progress"/>
    # 经验证也不是需要生命周期属性，不知道该方法如何使用
    from pm4py.statistics.sojourn_time.log.get import apply as sojourn_time
    sojourn_time = sojourn_time(log)
    print(sojourn_time)
    # 也不知道该方法怎么用
    from pm4py.statistics.traces.cycle_time.log.get import apply as cycle_time
    cycle_time = cycle_time(log)
    print(cycle_time)
    # 前后事件经过的时间
    from pm4py.statistics.passed_time.log.algorithm import apply as passed_time
    from pm4py.statistics.passed_time.log import variants
    passed_time = passed_time(log, 'decide', variant=variants.prepost)
    print(passed_time)


if __name__ == '__main__':
    log = xes_importer('../statics/log/running-example.xes')
    # log = xes_importer('../statics/log/receipt.xes')
    # log = xes_importer('../statics/log/BPI_Challenge_2013_closed_problems.xes')

    time_info(log)
    # todo
    # print(get_events_distribution(log))
