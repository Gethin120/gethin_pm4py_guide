from pm4py.objects.log.importer.xes.importer import apply as xes_importer

# log = xes_importer('../statics/log/running-example.xes')
log = xes_importer('../statics/log/receipt.xes')
# print(log)
from pm4py.algo.transformation.log_to_features import algorithm as log_to_features

data, feature_names = log_to_features.apply(log)
print(feature_names)
feature_set=[]
for i in feature_names:
    feature_set.append(i.split('@')[0])
print(set(feature_set))

import pandas as pd

df = pd.DataFrame(data, columns=feature_names)
from sklearn.decomposition import PCA

pca = PCA(n_components=5)
df2 = pd.DataFrame(pca.fit_transform(df))
print(df2)

import os
import pm4py
from pm4py.algo.transformation.log_to_features.util import locally_linear_embedding
from pm4py.visualization.graphs import visualizer

# log = pm4py.read_xes(os.path.join("tests", "input_data", "receipt.xes"))
x, y = locally_linear_embedding.apply(log)
gviz = visualizer.apply(x, y, variant=visualizer.Variants.DATES,
                        parameters={"title": "Locally Linear Embedding", "format": "svg", "y_axis": "Intensity"})
visualizer.view(gviz)