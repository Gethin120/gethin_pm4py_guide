import os
from pm4py.objects.log.importer.xes.importer import apply as xes_importer

log = xes_importer('../statics/log/receipt.xes')

print(log.classifiers)

from pm4py.objects.log.util import insert_classifier
log, activity_key = insert_classifier.insert_activity_classifier_attribute(log, "Activity classifier")
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
parameters = {alpha_miner.Variants.ALPHA_CLASSIC.value.Parameters.ACTIVITY_KEY: activity_key}
net, initial_marking, final_marking = alpha_miner.apply(log, parameters=parameters)