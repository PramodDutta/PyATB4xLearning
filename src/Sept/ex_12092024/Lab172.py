# OrderedDict
# Dictionary that remembers insertion order'
from collections import OrderedDict, defaultdict

d = dict() #Normal Dict order not maintained
d["age"] = 78
d["name"] = "pramod"
d["id"] = 43
d["address"] = "KA"
print(d)

od = OrderedDict()
od['banana'] = 2
od['apple'] = 1
od['pear'] = 3
print(od)

dd = defaultdict(int)
print(dd)

