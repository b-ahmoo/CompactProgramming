def list_exampple():
    sample_list = [1, 2, 3, 4, 5]
    for x in sample_list:
        print("Current number in list is: %d with index %d " % (x, sample_list.index(x)))

    for x in range(len(sample_list)):
        print("Current number in list is: %d with index %d " % (sample_list[x], x))

def tuple_example():
    sample_tuple = (1,2,3, 'a', 'ab', 'abc', (1,2), (1,3))
    print("item at index 3 = ",sample_tuple[3])
    print("item at index 6 = ",sample_tuple[6])

    print("Length of tuple = ", len(sample_tuple))

    for x in sample_tuple:
        print("Current item in tuple is: %s with index %d " % (x, sample_tuple.index(x)))


def doubler(i): return i*i 

L=[1,2,3,4,5] 
result=map(doubler,L) 
print(list(result))


#tuple_example()
#list_exampple()