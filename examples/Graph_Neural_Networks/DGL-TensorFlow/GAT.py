import tensorflow as tf
import dgl
import graphgallery

print("GraphGallery version: ", graphgallery.__version__)
print("TensorFlow version: ", tf.__version__)
print("DGL version: ", dgl.__version__)

'''
Load Datasets
- cora/citeseer/pubmed
'''
from graphgallery.datasets import Planetoid
data = Planetoid('cora', root="~/GraphData/datasets/", verbose=False)
graph = data.graph
splits = data.split_nodes()

graphgallery.set_backend("dgl_tf")

from graphgallery.gallery import GAT
trainer = GAT(graph, device="gpu", seed=123).process(attr_transform="normalize_attr").build()
his = trainer.train(splits.train_nodes, splits.val_nodes, verbose=1, epochs=100)
results = trainer.test(splits.test_nodes)
print(f'Test loss {results.loss:.5}, Test accuracy {results.accuracy:.2%}')
