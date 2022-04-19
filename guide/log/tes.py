from pm4py.objects.log.importer.xes.importer import apply as xes_importer
log = xes_importer('create_log.xes')
print(log)