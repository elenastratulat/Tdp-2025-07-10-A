from model.category import Category
from model.model import Model

mymodel=Model()

c=Category(5, "Electric Bikes")
mymodel.buildGraph(c)
n, e = mymodel.getGraphDetails()
print(f"N nodi : {n}, N archi: {e}")