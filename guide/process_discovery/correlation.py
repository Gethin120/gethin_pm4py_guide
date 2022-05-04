"""
correlation miner 相关挖掘，不考虑案例仅考虑活动之间的相关关系，仅需活动和代表先后关系的时间戳
"""
import pandas as pd
import os
from pm4py.objects.log.util import dataframe_utils

df = pd.read_csv(os.path.join("../statics", "log", "receipt.csv"))
df = dataframe_utils.convert_timestamp_columns_in_df(df)
df = df[["concept:name", "time:timestamp"]]
print(df)
from pm4py.algo.discovery.correlation_mining import algorithm as correlation_miner

frequency_dfg, performance_dfg = correlation_miner.apply(df, parameters={
    correlation_miner.Variants.CLASSIC.value.Parameters.ACTIVITY_KEY: "concept:name",
    correlation_miner.Variants.CLASSIC.value.Parameters.TIMESTAMP_KEY: "time:timestamp"})
activities_freq = dict(df["concept:name"].value_counts())
from pm4py.visualization.dfg import visualizer as dfg_visualizer

gviz_freq = dfg_visualizer.apply(frequency_dfg, variant=dfg_visualizer.Variants.FREQUENCY,
                                 activities_count=activities_freq, parameters={"format": "svg"})
gviz_perf = dfg_visualizer.apply(performance_dfg, variant=dfg_visualizer.Variants.PERFORMANCE,
                                 activities_count=activities_freq, parameters={"format": "svg"})
dfg_visualizer.view(gviz_freq)
dfg_visualizer.view(gviz_perf)
