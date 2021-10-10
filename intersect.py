#Program Untuk Hitung Intersect 2 Term dan 3 Term
def intersect2term(term1,term2):
  store = []
  if term1 and term2 :
    for item in term1:
      if item in term2:
        store.append(item)
  return store

brutus = [1,2,4,11,31,45,173,174]
calpurnia = [2,31,54,101]
    
intersect2term(brutus,calpurnia)

def intersect3term(term1,term2,term3):
  store = []
  if term1 and term2 and term3 :
    for item in term1:
      for item in term2:
        if item in term3:
          if item in store:
            break
          store.append(item)
  return store
brutus = [1,2,4,11,31,45,173,174]
caesar = [2,31,54,101]
calpurnia = [5,31]
intersect3term(brutus,calpurnia,caesar)
