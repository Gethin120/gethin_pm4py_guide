"""
日志分割，可以用来拆分训练集和测试集，也可以用来简化较大日志简化计算。
"""

# from pm4py.ml import split_train_test
from pm4py.objects.log.util.split_train_test import split
from pm4py.objects.log.importer.xes.importer import apply as xes_importer

log = xes_importer('../statics/log/receipt.xes')
print(len(log))
training_log, test_log = split(log, train_percentage=0.8)  # 分割比例默认是0.8，顺序分割

print(len(training_log))
