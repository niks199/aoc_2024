def all_threes_with_t(inp: str):
    edges = [ee.split('-') for ee in inp.splitlines()]

    adj_list = {}

    for (a, b) in edges:
        adj_list.setdefault(a, [])
        adj_list.setdefault(b, [])
        adj_list[a].append(b)
        adj_list[b].append(a)

    triples = set()   

    seen = set()


    for start_v in adj_list.keys():
        if start_v in seen:
            continue
        dfs(adj_list, start_v, 2, [start_v], triples, seen)

        seen.add(start_v)

    triples = sorted(triples)

    #print(*triples, sep='\n')
    
    c = 0
    for ts in triples:
        for t in ts:
            if t.startswith('t'):
                c += 1
                break
    
    return c

def dfs(adj_list, v: str, c: int, path: list, triples: set, seen: set):
    seen.add(v)

    if c == 0:
        seen.remove(v)
        if path[0] in adj_list[v]:
            p_c = path[:]
            p_c.sort()
            triples.add(tuple(p_c))
        return
        
    for neigh in adj_list[v]:
        if neigh not in seen:
            dfs(adj_list, neigh, c - 1, path + [neigh], triples, seen)

    seen.remove(v)

def bron_kerbosch(r: set, p: set, x: set, adj_list: dict):
    cliques = set()
    if not p and not x:
        cliques.add(frozenset(r))
    
    while p:
        v = p.pop()
        sub_cliques = bron_kerbosch(
            r.union({v}), 
            p.intersection(adj_list[v]),
            x.intersection(adj_list[v]), 
            adj_list)
        for sub_clique in sub_cliques:
            cliques.add(frozenset(sub_clique))
        x.add(v)

    return cliques

def password(inp: str):
    edges = [ee.split('-') for ee in inp.splitlines()]

    adj_list = {}

    for (a, b) in edges:
        adj_list.setdefault(a, set())
        adj_list.setdefault(b, set())
        adj_list[a].add(b)
        adj_list[b].add(a)

    cliques = bron_kerbosch(set(), set(adj_list.keys()), set(), adj_list)

    max_clique = set()
    for cl in  cliques:
        if len(cl) > len(max_clique):
            max_clique = cl

    max_clique_l = list(max_clique)
    max_clique_l.sort()
    pwd = ','.join(max_clique_l)

    return pwd
