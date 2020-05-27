import datetime
def find(st, arr, i, visited):
    for idx, j in enumerate(arr):
        if visited[idx]:
            continue
        if j[i] == st:
            return [[j, idx]]

def dfs(visited, arr, start, idToQuery, idToInsert):
    st = [start]
    z_elems = []
    while (st):
        ele = st.pop()
        a = find(ele, arr, idToQuery, visited)
        if a:
            if visited[a[0][1]]:
                continue
            visited[a[0][1]] = True
            z_elems.append(a[0][0][idToInsert])
            st.append(a[0][0][idToInsert])
    return z_elems

def findWord(*args):
    resultString = []
    visited = [False]*len(args[0])
    for idx, i in enumerate(args[0]):
        if visited[idx]:
            continue
        z_elems = dfs(visited, args[0], i[0], 2, 0)
        n_elems = dfs(visited, args[0], i[2], 0, 2)
        stringToAppend = i
        for z_elem in z_elems:
            stringToAppend = z_elem +">" +stringToAppend
        for n_elem in n_elems:
            stringToAppend = stringToAppend+">"+n_elem
        resultString.append(stringToAppend)

    print(resultString[0].replace('>', ''))

start = datetime.datetime.now()
findWord(["P>E","E>R","R>U"]) # PERU
findWord(["I>N","A>I","P>A","S>P"]) # SPAIN
findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]) #HUNGARY
findWord(["I>F", "W>I", "S>W", "F>T"]) # SWIFT
findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]) # PORTUGAL
findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]) # SWITZERLAND
