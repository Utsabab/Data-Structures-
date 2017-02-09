from collections import deque

G = {}
G["A"] = ["B", "C"]
G["B"] = ["C", "D", "E"]
G["C"] = ["D"]
G["D"] = []
G["E"] = []

#BFS:
def printing(name):
  print_queue = deque()
  print_queue += name
  searched = []
  while print_queue:
    person = print_queue.popleft()
    print(person)
    for i in G[person]:
      if i not in searched:
        print_queue.append(i)
        searched.append(i)

printing("A")

