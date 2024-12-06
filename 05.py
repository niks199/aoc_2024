class Solution:
    def middle_pages(self, inp: str):
        rules = []
        update_pages = []
        pa1 = True
        lines = inp.splitlines()
        for line in lines:
            if not line:
                pa1 = False
            else:
                if pa1:
                    v = line.split('|')
                    t = (int(v[0]), int(v[1]))
                    rules.append(t)
                else:
                    pp = [int(g)for g in line.split(',')]
                    update_pages.append(pp)
    
        adj_list = {}

        for rule in rules:
            adj_list.setdefault(rule[0], set())
            adj_list.setdefault(rule[1], set())
            adj_list[rule[0]].add(rule[1])
        
        tot = 0
        for update_page in update_pages:
            m = len(update_page)
            correct_page = True
            for page_i in range(1, m):
                p_num = update_page[page_i - 1]
                if update_page[page_i] not in adj_list[p_num]:
                    correct_page = False
                    break
            if correct_page:
                mid = (m // 2)
                tot += update_page[mid]

        return tot


    def incorrect_middle_pages(self, inp: str):
        rules = []
        update_pages = []
        pa1 = True
        lines = inp.splitlines()
        for line in lines:
            if not line:
                pa1 = False
            else:
                if pa1:
                    v = line.split('|')
                    t = (int(v[0]), int(v[1]))
                    rules.append(t)
                else:
                    pp = [int(g)for g in line.split(',')]
                    update_pages.append(pp)
    
        adj_list = {}

        for rule in rules:
            adj_list.setdefault(rule[0], set())
            adj_list.setdefault(rule[1], set())
            adj_list[rule[0]].add(rule[1])
        
        tot = 0
        for update_page in update_pages:
            m = len(update_page)
            correct_page = True
            for page_i in range(1, m):
                p_num = update_page[page_i - 1]
                if update_page[page_i] not in adj_list[p_num]:
                    correct_page = False
                    break
            if not correct_page:
                adj_list_cut = {}
                for page in update_page:
                    adj_list_cut[page] = adj_list[page]

                res = []
                seen = set()
                for k, bb in adj_list_cut.items():
                    if k not in seen:
                        self.topo(adj_list_cut, k, res, seen)
                res.reverse()

                mid = (m // 2)
                tot += res[mid]

        return tot
    
    def topo(self, adj_list, v, res, seen):
        seen.add(v)
        if v in adj_list:
            for ad in adj_list[v]:
                if ad not in seen:
                    self.topo(adj_list, ad, res, seen)
            res.append(v)
