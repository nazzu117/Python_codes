import csv
def deviation_score (issue_counts):
    issue_dis=[i/sum (issue_counts) for i in issue_counts] 
    min_dis float("inf")
    for i in range(len(issue_dis)-1):
        for j in range (i+1,len (issue_dis)): diff=abs(issue_dis [i]-issue_dis[j])
        if diff==1:
            return diff
            if min_dis>diff: min_dis=diff
        print("Min_diff"_min_dis)

    return min_dis