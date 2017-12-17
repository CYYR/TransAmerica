include "Steiner_Tree.mzn";

int: nbV;
int: nbE;
set of int: nodes = 1..nbV;
set of int: edges = 1..nbE;
set of int: terminals;

array [nodes] of var 0..1: vs;
array [edges] of var 0..1: es;
array [nodes, edges] of bool: map;
array [edges, nodes] of bool: endnodes;
array [edges] of int: link_cost;

%terminals constraint
constraint forall (i in index_set(terminals)) (vs[terminals[i]] == 1);

%chosing an edge will make trigger the chosing of nodes
constraint forall (e in edges) (forall (n in nodes) ((es[e] = 1 /\ endnodes [e, n]) -> vs[n] = 1));

%Every chosen node should have at least a chosen incident edge
constraint forall (n in nodes) ((vs[n] = 1) -> (exists (e in edges) ((map[n, e]) /\ (es[e] = 1) )));

%the basic neccessary condition for being a tree
constraint sum (i in edges) (es[i]) = sum(i in nodes)(vs[i]) - 1;

constraint forall (n1, n2 in index_set(terminals)) (path_exist (vs, es, map, endnodes, n1, n2));

solve minimize sum (i in edges) (es[i] * link_cost[i])
