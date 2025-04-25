def fcfcs(pageRef,n):
    pages = []
    hits = 0
    idx = 0
    for p in pageRef:
        if p in pages:
            hits+=1
            print(f"Page Hits")
        else:
            if len(pages)<n:
                pages.append(p)
            else:
                pages[idx]=p
                idx = (idx+1)%n
            print(f"{pages} MISS")
    return hits

def lru(pageRef,n):
    pages = []
    hits = 0
    idx = 0 
    for p in pageRef:
        if p in pages:
            hits+=1
            pages.remove(p)
            pages.append(p)
            print(f"Page Hit")
        else:
            if len(pages)<n:
                pages.append(p)
            else:
                pages.pop(0)
                pages.append(p)
            print(f"Page Miss")
    return hits

def optimal(pageref,n):
    pages = []
    hits = 0
    for i in range(len(pageRef)):
        p = pageRef[i]
        if p in pageRef:
            hits+=1
            print(f"Page Hit")
        else:
            if len(page)<n:
                page.append(p)
            else:
                future = pageRef[i+1:]
                indexes=[]
                for b in page:
                    if b in future:
                        indexes.append(future.index(b))
                    else:
                        indexes.append(float('inf'))
                replace_idx = indexes.index(max(indexes))
                page[replace_idx] = p
                print(f"Page Miss")
    return hits

pageRef = [5, 0, 2, 3, 1, 3, 0, 2, 3, 1, 2, 0, 5, 3, 2]
n = 3

print("FCFS Hits:", fcfcs(pageRef, n))
print("LRU Hits:", lru(pageRef, n))
print("Optimal Hits:", optimal(pageRef, n))



          