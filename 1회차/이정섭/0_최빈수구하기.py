
t = int(input()) # input # of total cases
n = int(input()) # Input the # of test case
score_list = [] # make list for upcoming score input
for scores in range (t): 
    score = map(int, input().split()) # acknowlege inputs as integer
    score_list.append(score)
    score_list.count(score) # use count method to figure out mos frequent score
                            # try to use length method on count.

print(t,f'#{n} {score}')    # Use f'string to print out both number of test case and the frequent score.