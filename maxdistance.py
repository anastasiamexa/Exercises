import itertools
# The function needs 2 parameters a string and a number
def maxDistance(string,num):
    l=[]
    int(num)
    for i in range(0,len(string)+1):
        # Finds all the combinations
        for j in itertools.combinations(string,i):
            s = sum(j)
            if s <= num:
                # Creates a list with all possible sums
                l.append(s)
    # Picks the bigger one
    print (max(l))

# Calls the function
maxDistance([64,8,87,10,2],22)