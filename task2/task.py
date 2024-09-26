import csv
from collections import defaultdict


def main(csv_file):
    graph = defaultdict(list)
    maxim = 0
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)        
        for row in reader:
            parent, child = int(row[0]), int(row[1])
            if parent > maxim: maxim = parent
            if child > maxim: maxim = child
            graph[parent].append(child)


    relations = ['r1', 'r2', 'r3', 'r4', 'r5']
    result = []
    for node in range(1, maxim+1):
        extensional_lengths = []
        for relation in relations:
            count = 0
            if relation == 'r1':
                for child in graph[node]:
                    if child in graph[node]:
                        count += 1
            elif relation == 'r2':
                for parent, children in graph.items():
                    if node in children:
                        count += 1
            elif relation == 'r3':
                for child in graph[node]:
                    for grandchild in graph[child]:
                        if grandchild in graph[child]:
                            count += 1
            elif relation == 'r4':
                for parent, children in graph.items():
                    if node not in graph[parent] and parent == 1 and node != 1:
                        count += 1
            elif relation == 'r5':
                for parent, children in graph.items():
                    if node in children and parent != node:
                        for sibling in children:
                            if sibling != node and sibling in graph:
                                count += 1
            extensional_lengths.append(str(count))
        result.append(','.join(extensional_lengths))

    return '\n'.join(result)




csv_file = "C:/Users/n8122/Downloads/task2.csv"
result = main(csv_file)
print('\n', result)
# csv_string = "A,B\nB,C\nB,D\nD,E"
# result = main(csv_string)
# print(result)