#!/usr/bin/env python3
import sys

# Get function arguments
file_name = str(sys.argv[1])
threshold = int(str(sys.argv[2]))

import time

file = open(file_name, "r")

start = time.time()
adj_dict = {}
node_dict = {}

data=file.readline()

class node:
  def __init__(self, val, dist, color, parent, contacts, influenced):
    self.val = val
    self.dist = dist
    self.color = color
    self.parent = parent
    self.contacts = contacts
    self.influenced = influenced

while data:
  [u, v, weight] = data.split()
  u = int(u)
  v = int(v)
  weight = float(weight)

  u_node = node(u, 999999, "W", None, 1, False)
  v_node = node(v, 999999, "W", None, 1, False)

  if u not in node_dict:
    node_dict[u] = u_node
  if v not in node_dict:
    node_dict[v] = v_node

  if u not in adj_dict.keys():
    adj_dict[u] = [[v, weight]]
  else:
    adj_dict[u].append([v, weight])

  data=file.readline()

queue = []
influenced = []
def BFS_with_limits(source_num, time, debug = False):
  for nodes in node_dict.keys():
    node_dict[nodes].color = "W"
    node_dict[nodes].dist = 999999
    node_dict[nodes].parent = None
    node_dict[nodes].contacts = 1
    node_dict[nodes].influenced = False

  influenced.clear()
  # iterate_adj_list()

  source_node = node_dict[source_num]
  source_node.color = "G"
  source_node.dist = 0
  queue.append(source_num)

  while len(queue) > 0:
    new_num = queue.pop(0)
    source_num
    if debug:
      print("Exploring node:", new_num)
    if (new_num in adj_dict.keys()):
      for neighbour in adj_dict[new_num]:
        node = node_dict[neighbour[0]]
        weight = neighbour[1]

        if (node.color == "W" and ((weight + node_dict[new_num].dist) <= time)):
          if debug:
            print("Reached node:", node.val, "time take:", (weight + node_dict[new_num].dist))
          node_dict[source_num].contacts += 1
          node.color = "G"
          node.dist = node_dict[new_num].dist + weight
          node.parent = new_num
          queue.append(node.val)
          influenced.append(node.val)
      node_dict[new_num].color = "B"
    else:
      pass

  if debug:
    print(source_num, "has", node_dict[source_num].contacts, "contacts")
  return node_dict[source_num].contacts

max_contacts = -1
influencer = -1
for nodes in node_dict.keys():
  res = BFS_with_limits(nodes, threshold)
  #print("Node:", nodes, "Res:", res)
  if (max_contacts < res):
    max_contacts = res
    influencer = nodes
    top_influencer = influenced.copy()

end = time.time()
print("TOP-1 INFLUENCER:", str(influencer) + ", SPREAD:", str(max_contacts) + ", TIME:", str(end-start), "sec")
#print(top_influencer)
#print(len(top_influencer))

start2 = time.time()
def BFS_with_limits_Top2(source_num, time, debug = False):
  for nodes in node_dict.keys():
    node_dict[nodes].color = "W"
    node_dict[nodes].dist = 999999
    node_dict[nodes].parent = None
    node_dict[nodes].contacts = 1
    if nodes in top_influencer: #if node exists in top influencer, then set influenced to true
      node_dict[nodes].influenced = True
    else:
      node_dict[nodes].influenced = False
    if source_num in top_influencer:
      node_dict[source_num].contacts = 0

  # iterate_adj_list()

  source_node = node_dict[source_num]
  source_node.color = "G"
  source_node.dist = 0
  queue.append(source_num)

  while len(queue) > 0:
    new_num = queue.pop(0)
    source_num
    if debug:
      print("Exploring node:", new_num)
    if (new_num in adj_dict.keys()):
      for neighbour in adj_dict[new_num]:
        node = node_dict[neighbour[0]]
        weight = neighbour[1]

        if (node.color == "W" and ((weight + node_dict[new_num].dist) <= time)):
          if debug:
            print("Reached node:", node.val, "time take:", (weight + node_dict[new_num].dist))
          if node.influenced == False:
            node_dict[source_num].contacts += 1
          node.color = "G"
          node.dist = node_dict[new_num].dist + weight
          node.parent = new_num
          queue.append(node.val)
      node_dict[new_num].color = "B"
    else:
      pass

  if debug:
    print(source_num, "has", node_dict[source_num].contacts, "contacts")
  return node_dict[source_num].contacts

max_contacts_2 = -1
influencer_2 = -1
for nodes in node_dict.keys():
  if nodes != influencer:
    res = BFS_with_limits_Top2(nodes, threshold)
    if (max_contacts_2 < res):
      max_contacts_2 = res
      influencer_2 = nodes

end2 = time.time()

print("TOP-2 INFLUENCER:", str(influencer_2) + ", MARGINAL SPREAD:", str(max_contacts_2) + ", TIME:", str(end2-start2), "sec")
