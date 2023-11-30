#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    nm = dir(hidden_4)
    for i in range(len(nm)):
        if nm[i][0] != "_" and nm[i][1] != "_":
            print(nm[i])
