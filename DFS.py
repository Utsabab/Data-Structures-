G = {}
G["A"] = ["B", "C"]
G["B"] = ["C", "D", "E"]
G["C"] = ["D"]
G["D"] = []
G["E"] = []

#DFS:
def printing(root):
  stack = []
    stack += root
  searched = []
  while stack:
    person = stack.pop()
    print(person)
    for i in G[person]:
      if i not in searched:
        stack.append(i)
        searched.append(i)
printing("A")