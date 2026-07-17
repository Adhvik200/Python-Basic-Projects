test_graph_1 = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

def adjacency_list_to_matrix(dict):
    V = len(dict)
    adj_matrix = [[0] * V for _ in range(V)]
    
    for u in range(V):
        for v in dict[u]:
            adj_matrix[u][v] = 1
            
    for row in adj_matrix:
        print(row)
        
    return adj_matrix

matrix_1 = adjacency_list_to_matrix(test_graph_1)