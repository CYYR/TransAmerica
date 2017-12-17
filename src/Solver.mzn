int: nbV;
int: nbE;
var int: w;
set of int: nodes = 1..nbV;
set of int: edges = 1..nbE;
set of int: terminals;

array [nodes] of var 0..1: vs;
array [nodes] of var -1..nbV: father_node;
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

constraint father_node[min(terminals)]=min(terminals);

%Every chosen node should has a father node, and vice versa
constraint forall (n in nodes) (vs[n]=1 <-> father_node[n]>0);
constraint forall (n in nodes) (vs[n]=0 <-> father_node[n]=0);

predicate connected_node (int: n1, int: n2) = exists (e in edges) (endnodes[e,n1] /\ endnodes[e,n2]);

predicate chosen (int: n1) = vs[n1]=1;

constraint forall (n1, n2 in nodes where not(n1=min(terminals))) (father_node[n1]=n2 -> chosen(n2) /\ not (father_node[n2]=n1) /\ connected_node(n1,n2));

constraint forall (e in edges) (forall (n1, n2 in nodes where not(n1=min(terminals))) ((endnodes[e,n1] /\ endnodes[e,n2] /\ father_node[n1]=n2) -> es[e]=1));

constraint w = sum (i in edges) (es[i] * link_cost[i]);

solve minimize w;
