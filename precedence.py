# from
import datetime
def find(st, arr, i, visited):
    for idx, j in enumerate(arr):
        if visited[idx]:
            continue
        if j[i] == st:
            return [[j, idx]]

def findWord(*args):
    resultString = []
    visited = [False]*len(args[0])
    for idx, i in enumerate(args[0]):
        if visited[idx]:
            continue
        st = [i[0]]
        z_elems = []
        while (st):
            ele = st.pop()
            a = find(ele, args[0], 2, visited)
            if a:
                if visited[a[0][1]]:
                    continue
                visited[a[0][1]] = True
                z_elems.append(a[0][0][0])
                st.append(a[0][0][0])

        n_elems = []
        st = [i[2]]
        while (st):
            ele = st.pop()
            a = find(ele, args[0], 0, visited)
            # print(a)
            if a:
                if visited[a[0][1]]:
                    continue
                visited[a[0][1]] = True
                st.append(a[0][0][2])
                n_elems.append(a[0][0][2])

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
