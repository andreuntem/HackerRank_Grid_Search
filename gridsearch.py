def gridSearch(G, P):
    print(G)
    print(P)

if __name__ == '__main__':
    raw_inp = '''
    10 10
    7283455864
    6731158619
    8988242643
    3830589324
    2229505813
    5633845374
    6473530293
    7053106601
    0834282956
    4607924137
    3 4
    9505
    3845
    3530
    '''
    inp = raw_inp.split() 
    r_grid, c_grid = int(inp[0]), int(inp[1])
    r_pat, c_pat = int(inp[r_grid+2]), int(inp[r_grid+3])

    G = []
    for i in range(r_grid):
        G.append(inp[i+2])
    
    P = []
    for i in range(r_pat):
        P.append(inp[r_grid+4])

    gridSearch(G,P)