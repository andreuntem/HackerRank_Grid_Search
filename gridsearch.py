from collections import Counter

def gridSearch(G, P):

    # flatten pattern
    pattern = ''.join(P)
    #counter_pattern = Counter(pattern)
    
    # Length grid and pattern
    r_grid, c_grid = len(G), len(G[0])
    r_pat, c_pat = len(P), len(P[0])
    #size_pat = r_pat*c_pat
    
    # Check by subgrid:
    found = 'NO'
    for i in  range(r_grid - r_pat + 1):
        for j in range(c_grid - c_pat + 1):
            
            # Define subgrid
            subgrid = [G[i+k][j:j+c_pat] for k in range(r_pat)]
            subgrid = ''.join(subgrid)
            #counter_subgrid = Counter(subgrid)

            if subgrid == pattern:
                found = 'YES'
                break

            '''
            if counter_subgrid == counter_pattern:
                diff = [pattern[ix] == subgrid[ix] for ix in range(size_pat)]
                if all(diff) == True:
                    found = 'YES'
                    break
            '''
        if found == 'YES':
            break

    return found

if __name__ == '__main__':
    raw_inp = '''
    4 6
    123412
    561212
    123634
    781288
    2 2
    12
    34
    '''
    inp = raw_inp.split() 
    r_grid, c_grid = int(inp[0]), int(inp[1])
    r_pat, c_pat = int(inp[r_grid+2]), int(inp[r_grid+3])

    G = []
    for i in range(r_grid):
        G.append(inp[i+2])
    
    P = []
    for i in range(r_pat):
        P.append(inp[i+r_grid+4])

    print(gridSearch(G,P))