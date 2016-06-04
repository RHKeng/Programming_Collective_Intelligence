

def Manhattan_distance(blog1,blog2):
    sum=0
    for i in range(len(blog1)):
        sum+=float(abs(blog1[i]-blog2[i]))

    return sum