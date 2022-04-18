""""
导入日志，输入格式一般为xes或csv
"""
#导入xes格式日志
from pm4py.objects.log.importer.xes.importer import apply as xes_importer
log = xes_importer('../statics/log/receipt.xes')
print(log)

#导入csv格式日志
import pandas as pd
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter

log_csv = pd.read_csv('../statics/log/receipt.csv', sep=',')
log_csv = dataframe_utils.convert_timestamp_columns_in_df(log_csv)
log_csv = log_csv.sort_values('time:timestamp')
log = log_converter.apply(log_csv)
print(log)