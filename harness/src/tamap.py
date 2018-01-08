
import sys

def lrange(fr, to):
    return list(range(fr, to + 1))

nodes = [lrange(2, 11),              # 1
         lrange(1, 12) + [16,17],    # 2
         lrange(1, 13) + [16,17,18], # 3
         lrange(1, 17),              # 4
         lrange(1, 17),              # 5
         lrange(1, 16),              # 6
         lrange(1, 16),              # 7
         lrange(1, 16),              # 8
         lrange(2, 17),              # 9
         lrange(2, 16),              # 10
         lrange(3, 16),              # 11
         lrange(4, 15),              # 12
         lrange(7, 15)]              # 13

## if row is odd, then
##   dir=1 goes to (row + 1, col)
##   dir=2 goes to (row + 1, col - 1)

## if row is even, then
##   dir=1 goes to (row + 1, col + 1)
##   dir=2 goes to (row + 1, col)

## dir=0 goes to (row, col + 1)

dlinks = (
    # row 1
    (1,2,0), (1,2,1),
    (1,4,2),
    (1,6,1), (1,6,2),
    (1,7,1), (1,7,2),
    (1,8,2),
    # row 2
    (2,1,0), (2,1,1),
    (2,3,0),
    (2,4,0), (2,4,2),
    (2,5,2),
    (2,7,0),
    (2,8,2),
    (2,10,0),
    (2,11,2),
    # row 3
    (3,1,0),
    (3,2,2),
    (3,4,0),
    (3,5,0),
    (3,6,2),
    (3,8,0),
    (3,9,2),
    (3,11,0),
    (3,12,2),
    # row 4
    (4,1,0),
    (4,1,1),
    (4,5,0),
    (4,7,0),
    (4,8,2),
    (4,10,0), (4,10,1),
    (4,15,1),
    # row 5
    (5,1,0),
    (5,2,2),
    (5,3,2),
    (5,5,2),
    (5,9,0),
    (5,10,2),
    (5,11,0),
    (5,12,2),
    (5,16,0), (5,16,1),
    # row 6
    (6,1,0), (6,1,1),
    (6,2,0), (6,2,1),
    (6,4,1),
    (6,5,0), (6,5,2),
    (6,6,2),
    (6,9,0),
    (6,10,1), (6,10,2),
    (6,11,0), (6,11,1), (6,11,2),
    (6,12,2),
    (6,13,1),
    (6,14,1), (6,14,2),
    (6,15,0), (6,15,1),
    # row 7
    (7,2,0), (7,2,2),
    (7,4,0), (7,4,1),
    (7,6,0), (7,6,1),
    (7,12,0),
    (7,13,0), (7,13,1), (7,13,2),
    (7,15,0), (7,15,1),
    # row 8
    (8,1,0),
    (8,3,0), (8,3,1),
    (8,5,0),
    (8,12,0), (8,12,1),
    (8,14,0), (8,14,1),
    # row 9
    (9,2,0),
    (9,3,0),
    (9,4,0), (9,4,2),
    (9,5,2),
    (9,12,0), (9,12,1),
    (9,14,0), (9,14,1),
    # row 10
    (10,2,0),
    (10,3,0), (10,3,1),
    (10,4,0),
    (10,5,1), (10,5,2),
    (10,11,0), (10,11,1),
    (10,13,0),
    # row 11
    (11,3,0),
    (11,11,0),
    (11,12,2),
    # row 12
    (12,11,0), (12,11,1),
    # row 13
    (13,11,0)
    )

c_green = ((1,2), (2,1), (4,1), (6,1), (7,1), (10,2), (11,3))
n_green = ("Seattle", "Portland", "Medford", "Sacramento", "San Fransisco", "Los Angeles", "San Diego")
c_blue = ((2,4), (2,8), (2,11), (3,11), (3,16), (4,13), (6,14))
n_blue = ("Helena", "Bismarck", "Duluth", "Minneapolis", "Buffalo", "Chicago", "Cincinnati")
c_yellow = ((5,4), (5,9), (6,6), (7,10), (7,12), (9,6), (9,9))
n_yellow = ("Salt Lake City", "Omaha", "Denver", "Kansas City", "St Louis", "Santa Fe", "Oklahoma City")
c_red = ((10,4), (10,12), (11,10), (11,14), (12,6), (13,10), (13,12))
n_red = ("Phoenix", "Memphis", "Dallas", "Atlanta", "El Paso", "Houston", "New Orleans")
c_orange = ((3,18), (5,17), (6,16), (8,16), (9,15), (11,16), (13,15))
n_orange = ("Boston", "New York", "Washington", "Richmond", "Winston", "Charleston", "Jacksonville")

# def print_map(m):
#     for rnum,row in enumerate(m):
#         s = ''
#         l = ''
#         if (rnum + 1) % 2 == 0:
#             s += ' '
#         for col in range(1, max(row) + 1):
#             if col in row:
#                 if (rnum + 1, col - 1, 0) in dlinks_list:
#                     s += '-*'
#                 else:
#                     s += ' *'
#                 if (rnum + 1, col - 1, 2) in dlinks:
#                     l += '/'
#                 else:
#                     l += ' '
#                 if (rnum + 1, col - 1, 1) in dlinks:
#                     l += '\\'
#                 else:
#                     l += ' '
#             else:
#                 s += '  '
#                 l += '  '
#         print(s)
#         print(l)

def adjacent_node(rn1, cn1, rn2, cn2):
    if rn2 > len(nodes):
        return False;
    if cn2 not in nodes[rn2 -1]:
        return False;

def print_adjacency(rn1, cn1, dirn, rn2, cn2, indent = 0, to = sys.stdout):
    if rn2 > len(nodes):
        return
    if cn2 not in nodes[rn2 - 1]:
        return
    if (rn1, cn1, dirn) in dlinks:
        cost = 2
    else:
        cost = 1
    print(" " * indent + "(adjacent node_" + str(rn1) + "_" + str(cn1) +
          " node_" + str(rn2) + "_" + str(cn2) + ")", file=to)
    print(" " * indent + "(adjacent node_" + str(rn2) + "_" + str(cn2) +
          " node_" + str(rn1) + "_" + str(cn1) + ")", file=to)
    print(" " * indent + "(= (link_cost node_" + str(rn1) + "_" + str(cn1) +
          " node_" + str(rn2) + "_" + str(cn2) + ") " + str(cost) + ")", file=to)
    print(" " * indent + "(= (link_cost node_" + str(rn2) + "_" + str(cn2) +
          " node_" + str(rn1) + "_" + str(cn1) + ") " + str(cost) + ")", file=to)

def from_line_to_node(lineN):
    row = 1
    for i in nodes:
        if lineN > len(i):
            row += 1
            lineN -= len(i)
        else:
            return row, i[lineN-1]

def adjacency(firstNode, secondNode):
    row1 = firstNode[0]
    col1 = firstNode[1]
    row2 = secondNode[0]
    col2 = secondNode[1]

    if (row1 == row2) and ((col1 == col2 + 1) or (col2 == col1 + 1)):
        return True
    if (row1 == row2 - 1):
        if (row1 % 2 == 1):
            return (col1 - 1 == col2) or (col1 == col2)
        else:
            return (col1 + 1 == col2) or (col1 == col2)
    if (row2 == row1 - 1):
        if (row2 % 2 == 1):
            return (col2 - 1 == col1) or (col2 == col1)
        else:
            return (col2 + 1== col1) or (col2 == col1)
    return False


# def print_map():
#     print("(:objects")
#     for rnum,row in enumerate(nodes):
#         for cnum in range(1, max(row) + 1):
#             if cnum in row:
#                 print("  node_" + str(rnum) + "_" + str(cnum))
#     print(" )")
#
#     print("(:init")
#     for rnum,row in enumerate(nodes):
#         rnum = rnum + 1
#         for cnum in range(1, max(row) + 1):
#             if cnum in row:
#                 # dir=0
#                 print_adjacency(rnum, cnum, 0, rnum, cnum + 1)
#                 # if row is odd, then
#                 if rnum % 2 == 1:
#                     # dir=1 goes to (row + 1, col)
#                     print_adjacency(rnum, cnum, 1, rnum + 1, cnum)
#                     # dir=2 goes to (row + 1, col - 1)
#                     print_adjacency(rnum, cnum, 1, rnum + 1, cnum - 1)
#                 else:  # if row is even, then
#                     # dir=1 goes to (row + 1, col + 1)
#                     print_adjacency(rnum, cnum, 2, rnum + 1, cnum + 1)
#                     # dir=2 goes to (row + 1, col)
#                     print_adjacency(rnum, cnum, 2, rnum + 1, cnum)
#     print(" )")

def print_map_facts(indent = 0, to = sys.stdout):
    for rnum,row in enumerate(nodes):
        rnum = rnum + 1
        for cnum in range(1, max(row) + 1):
            if cnum in row:
                # dir=0
                print_adjacency(rnum, cnum, 0, rnum, cnum + 1, indent, to=to)
                # if row is odd, then
                if rnum % 2 == 1:
                    # dir=1 goes to (row + 1, col)
                    print_adjacency(rnum, cnum, 1, rnum + 1, cnum, indent, to=to)
                    # dir=2 goes to (row + 1, col - 1)
                    print_adjacency(rnum, cnum, 2, rnum + 1, cnum - 1, indent, to=to)
                else:  # if row is even, then
                    # dir=1 goes to (row + 1, col + 1)
                    print_adjacency(rnum, cnum, 1, rnum + 1, cnum + 1, indent, to=to)
                    # dir=2 goes to (row + 1, col)
                    print_adjacency(rnum, cnum, 2, rnum + 1, cnum, indent, to=to)

def print_reached_fact(node, indent = 0, to = sys.stdout):
    rnum, cnum = node
    print(" " * indent + "(reached node_" + str(rnum) + "_" + str(cnum) + ")", file=to)


def print_objects(indent = 0, to=sys.stdout):
    print(" " * indent + "(:objects", file=to)
    for rnum,row in enumerate(nodes):
        rnum = rnum + 1
        for cnum in range(1, max(row) + 1):
            if cnum in row:
                print(" " * indent + "  node_" + str(rnum) + "_" + str(cnum), file=to)
    print(" " * indent + " )", file=to)


def print_problem(g, b, y, r, o, to=sys.stdout):
    assert(0 <= g < len(c_green))
    assert(0 <= b < len(c_blue))
    assert(0 <= y < len(c_yellow))
    assert(0 <= r < len(c_red))
    assert(0 <= o < len(c_orange))

    print("(define (problem ta_" + str(g) + "_" + str(b) + "_" + str(y)
          + "_" + str(r) + "_" + str(o) + ")", file=to)
    print("  (:domain transamerica)", file=to)
    print_objects(indent = 2, to=to)
    print(file=to)
    print("  (:init", file=to)
    print_map_facts(indent = 4, to=to)
    print_reached_fact(c_green[g], indent = 4, to=to)
    print("    (= (total-cost) 0)", file=to)
    print("   )", file=to)
    print(file=to)
    print("  (:goal (and", file=to)
    print_reached_fact(c_blue[b], indent = 11, to=to)
    print_reached_fact(c_yellow[y], indent = 11, to=to)
    print_reached_fact(c_red[r], indent = 11, to=to)
    print_reached_fact(c_orange[o], indent = 11, to=to)
    print("          ))", file=to)
    print(file=to)
    print("  (:metric minimize (total-cost))", file=to)
    print(" )", file=to)

def evaluate_link_cost(node1, node2):
    if (node1[0] < node2[0]):
        row = node1[0]
        col = node1[1]
        colC = node2[1]
    elif (node1[0] > node2[0]):
        row = node2[0]
        col = node2[1]
        colC = node2[1]
    else:
        row = node1[0]
        col = min(node1[1], node2[1])
        return dlink_to_value(row, col, 0)
    if (row % 2 == 1):
        if colC == col - 1:
            return dlink_to_value(row, col, 2)
        else:
            return dlink_to_value(row, col, 1)
    else:
        if colC == col + 1:
            return dlink_to_value(row, col, 1)
        else:
            return dlink_to_value(row, col, 2)

def dlink_to_value(row, col, dirc):
    if (row, col, dirc) in dlinks:
        return "2"
    else:
        return "1"



def generate_endnode(node1, node2):
    lineValue = ["false"] * 188
    lineValue[node1-1] = "true"
    lineValue[node2-1] = "true"
    return lineValue

def print_dzn(g, b, y, r, o, to=sys.stdout):
    assert(0 <= g < len(c_green))
    assert(0 <= b < len(c_blue))
    assert(0 <= y < len(c_yellow))
    assert(0 <= r < len(c_red))
    assert(0 <= o < len(c_orange))

    print("nbV=188;", file=to)
    print("nbE=509;", file=to )
    to.write("map = [|"); to.flush()
    endnodes=[]
    link_cost=[]
    recording=[]
    maps = []
    for i in range(188):
        maps.append(["false"] * 509)
    for i in range(1, 189):
        for j in range(1, 189):
            if adjacency(from_line_to_node(i), from_line_to_node(j)):
                # generaete the endndoes list
                if not (((i,j) in recording) or ((j,i) in recording)):
                    recording.append((i,j))
                    temp = generate_endnode(i, j)
                    endnodes.append(temp)
                    link_cost.append(evaluate_link_cost(from_line_to_node(i), from_line_to_node(j)))
                    maps[i-1][len(link_cost) - 1] = "true"
                    maps[j-1][len(link_cost) - 1] = "true"
    for i in maps:
        to.write(",".join(i))
        if (i == maps[-1]):
            to.write("|];\n")
        else:
            to.write("\n|")

    to.write("endnodes=[|"); to.flush()
    for i in endnodes:
        to.write(",".join(i))
        if (i == endnodes[-1]):
            to.write("|];\n")
        else:
            to.write("\n|")
    terminals=[]
    to.write("terminals={")
    terminals.append(from_node_to_line(c_green[g]))
    terminals.append(from_node_to_line(c_blue[b]))
    terminals.append(from_node_to_line(c_yellow[y]))
    terminals.append(from_node_to_line(c_red[r]))
    terminals.append(from_node_to_line(c_orange[o]))
    to.write(",".join(terminals) + "};\n")

    to.write("link_cost=[")
    to.write(",".join(link_cost) + "];")
    to.flush()

def from_node_to_line(nodeP):
    row=nodeP[0] - 1
    col=nodeP[1]
    count = 0
    for i in range(row):
        count += len(nodes[i])
    count += nodes[row].index(col) + 1
    return str(count)


def generate_all(limit = 1):
    count = 0
    for g in range(len(c_green)):
        for b in range(len(c_blue)):
            for y in range(len(c_yellow)):
                for r in range(len(c_red)):
                    for o in range(len(c_orange)):
                        fo = open("transamerica" + str(count) + ".dzn", 'w')
                        print_dzn(g, b, y, r, o, to = fo)
                        fo.close()
                        count += 1
                        if count > limit:
                            return

if __name__ == '__main__':
    if len(sys.argv) > 5:
        g = int(sys.argv[1])
        assert 0 <= g <= 6
        b = int(sys.argv[2])
        assert 0 <= b <= 6
        y = int(sys.argv[3])
        assert 0 <= y <= 6
        r = int(sys.argv[4])
        assert 0 <= r <= 6
        o = int(sys.argv[5])
        assert 0 <= o <= 6
        print(", ".join([n_green[g], n_blue[b], n_yellow[y], n_red[r], n_orange[o]]))
    elif len(sys.argv) > 1:
        limit = int(sys.argv[1])
        generate_all(limit)
    else:
        print(sys.argv[0] + " <g> <b> <y> <r> <o> : map index to names")
        print(sys.argv[0] + " <N> : generate first N instances")
