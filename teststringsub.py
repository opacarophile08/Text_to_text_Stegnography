# Python code to demonstrate
# checking all char in a string  in another string


def allCharPresent(test_str, res):
    flag =True
    ind = []
    for i in res:
        if i in test_str:
            print (" present in GeeksforGeeks")
            #flag = flag & True
            ind.append(test_str.find(i))
        else :
            #print (" not present in GeeksforGeeks")
            #flag = flag & False
            #ind.clear()
            return False,[]
    # print(flag)
    return True,ind

test_str="Geeks for Geeks"
res = "sfrke"
f, enc = allCharPresent(test_str, res)
print(enc)
m=""
for i in enc:
    m+=test_str[i]
print(m)




# # using str.find() to test
# # for substring
# res = test_str.find("efrks")
# if res >= 0:
# 	print (" present in GeeksforGeeks")
# else :
# 	print (" not present in GeeksforGeeks")
