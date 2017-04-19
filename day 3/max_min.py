def find_max_min(number):   
    new_list=[]
    if max(number) == min(number):
        k=len(number)
        new_list.append(k)
        return new_list
    else:
        new_list.append(min(number))
        new_list.append(max(number))
        return new_list

print(find_max_min([4,4,4,4]))