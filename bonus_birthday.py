# Elves encrypting their message
RDM_STR = "ORHATPOPKATYSBARNITRESTTIERDAHEDTKCSAAZYSY"

# Advent of code vibe
def prime(x):
    if x in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        return True
    else:
        return False

# But leves are drunk, so the message is somewhat... blurry
print("".join([RDM_STR[x] for x in range(len(RDM_STR)) if prime(x)]))
