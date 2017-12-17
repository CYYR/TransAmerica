% Predicate for judgeing if a grapg is connected
%predicate (array [nodes] of var 0..1: vs, array [edges] of var 0..1: es, array [nodes, edges] of bool: map, array [edges, nodes] of bool: endnodes, int: node1, int: node2) = (vs[node1] = 1) /\ (vs[node2] = 1) /\

% Checking if there is a path between two nodes
predicate path_exist (array [nodes] of var 0..1: vs, array [edges] of var 0..1: es, array [nodes, edges] of bool: map, array [edges, nodes] of bool: endnodes, int: node1, int: node2) = exists (tempE in edges)
                                          (exists (tempN in nodes where map[node1, tempE] /\ es[tempE]=1)
                                           (trace ("testsdfsyhert\n",path_exist (vs, es, map, endnodes, tempN, node2)) ));

%predicate path_exist_helper (array [nodes] of var 0..1: vs, array [edges] of var 0..1: es, array [nodes, edges] of bool: map, array [edges, nodes] of bool: endnodes, int: node1, int: node2, int preEdge) = exists (e in edges) ()

%predicate connected (array [nodes] of var 0..1: vs, array [edges] of var 0..1: es, array [nodes, edges] of bool: map, array [edges, nodes] of bool: endnodes, set of int: terminals) = let (set of int: temp = diff(terminals, {min(terminals)})) in true;
