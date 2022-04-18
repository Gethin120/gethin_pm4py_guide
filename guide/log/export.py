"""
将日志对象导出到xes文件
"""
from pm4py.objects.log.importer.xes.importer import apply as xes_importer
log = xes_importer('../statics/log/receipt.xes')

from pm4py.objects.log.exporter.xes import exporter as xes_exporter
xes_exporter.apply(log, 'exported_log.xes')