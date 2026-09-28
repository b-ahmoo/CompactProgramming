# Write a Python program  to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.  Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 

def sort_list():
    sample_list= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
    n = len(sample_list)

    for x in range(n):
        for y in range(n -x - 1):
         if (sample_list[y][1] > sample_list[y+1][1]):
            sample_list[y], sample_list[y + 1] = sample_list[y + 1], sample_list[y]

    print(sample_list)


def sorted_list():
       sample_list= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
       sortedlist = sorted(sample_list, key = lambda x: x[-1] )
       print(sortedlist)
   

#sort_list()
sorted_list()