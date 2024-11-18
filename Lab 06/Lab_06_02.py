def my_zip(*args: list, strct: bool = False) -> list:
    if(strct and False in [len(args[i]) == len(args[i+1]) for i in range(len(args) - 1)]):
        print("ERROR: Unequal length of iterators")
        return None
    
    # get minimum length of iterables
    n = min([len(iterable) for iterable in args])
    listoftuples = list(tuple(iterable[i] for iterable in args) for i in range(n))
    return listoftuples

customerName = ["ABC", "Vivek", "Shubham"]
customerId = [1, 2, 3]
shoppingPoints = ["Kolkata market", "Zudio"]

zippedlist = my_zip(customerName, customerId, shoppingPoints)

print(zippedlist)



def my_sort(zipped_list: list, key: int = 0) -> list:
    sorted_zipped_list = [t for t in zipped_list]  #deep copy
    for i in range(len(sorted_zipped_list)):
        for j in range(i, len(sorted_zipped_list)):
            if(sorted_zipped_list[i][key] > sorted_zipped_list[j][key]):
                sorted_zipped_list[i], sorted_zipped_list[j] = sorted_zipped_list[j], sorted_zipped_list[i]

    return sorted_zipped_list


print(my_sort(zippedlist, 2))
