"""09 — Graph mathematics.
Topics: degree, paths, connectivity, trees, bipartite graphs, and adjacency representations.
"""


def degree_map(edges:list[tuple[int,int]])->dict[int,int]: raise NotImplementedError

def edge_count_from_degrees(degrees:list[int])->int: raise NotImplementedError

def is_valid_degree_sequence(degrees:list[int])->bool: raise NotImplementedError

def adjacency_list(edges:list[tuple[int,int]])->dict[int,list[int]]: raise NotImplementedError

def path_exists(edges:list[tuple[int,int]],start:int,target:int)->bool: raise NotImplementedError

def connected_components(nodes:list[int],edges:list[tuple[int,int]])->int: raise NotImplementedError

def is_tree(nodes:list[int],edges:list[tuple[int,int]])->bool: raise NotImplementedError

def is_bipartite(nodes:list[int],edges:list[tuple[int,int]])->bool: raise NotImplementedError

def count_triangles(edges:list[tuple[int,int]])->int: raise NotImplementedError

def shortest_unweighted_distance(edges:list[tuple[int,int]],start:int,target:int)->int: raise NotImplementedError

TESTS=[
("degree_map",([(1,2),(2,3)],),{1:1,2:2,3:1}),("edge_count_from_degrees",([1,2,1],),2),
("is_valid_degree_sequence",([2,2,2],),True),("adjacency_list",([(1,2),(1,3)],),{1:[2,3],2:[1],3:[1]}),
("path_exists",([(1,2),(2,3)],1,3),True),("connected_components",([1,2,3,4],[(1,2),(3,4)]),2),
("is_tree",([1,2,3],[(1,2),(2,3)]),True),("is_bipartite",([1,2,3],[(1,2),(2,3)]),True),
("count_triangles",([(1,2),(2,3),(1,3)],),1),("shortest_unweighted_distance",([(1,2),(2,3),(1,4),(4,3)],1,3),2)]

def main():
 print("\nSample tests\n"+"-"*50)
 for n,a,e in TESTS[:2]:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print("\nSample tests passed. Running all tests...\n\nFull test suite\n"+"-"*50)
 for n,a,e in TESTS:
  r=globals()[n](*a); assert r==e,f"{n}: expected {e}, got {r}"; print(f"[PASS] {n}")
 print(f"\nOK — {len(TESTS)} questions passed")
if __name__=="__main__": main()
