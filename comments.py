# Opening the file
with open('testfile.txt','r') as f:
    lines = f.readlines()
    # Removes the \n
    lines[:] = [line.rstrip('\n') for line in lines]
    # First it prints the file with comments
    print(lines)
    # Now deletes the comments at the start of the line
    lines = [x for x in lines if not x.startswith('#')]
    # Searching for other comments
    for i in range(len(lines)):
        tmp = lines[i]
        cnt = 0
        for j in range(len(tmp)):
            if tmp[j] == "'" or tmp[j] == '"':
                cnt+=1
            elif tmp[j] == '#':
                # If the number is even, then it is a comment
                if cnt%2 == 0:
                    lines[i] = tmp[:j]
                    break
    # Prints the file without comments
    print(lines)