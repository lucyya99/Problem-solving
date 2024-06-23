# ver1.
# input N, file name
N = int(input())
file_name_list =[]
for n in range(N):
    file_name_list.append(input())

search_same_name = list(file_name_list[0])

# compare
for n in range(N-1):
    file_name = list(file_name_list[n+1])
    str_length = len(search_same_name)
    for i in range(str_length):
        if search_same_name[i] == '?':
            continue
        if search_same_name[i] != file_name[i]:
            search_same_name[i] = '?'

print("".join(search_same_name))

# ver2.
N = int(input())
file_name = list(input())
str_length = len(file_name)
for n in range(N-1):
    next_file_name = list(input())
    for i in range(str_length):
        if file_name[i] == '?':
            continue
        if file_name[i] != next_file_name[i]:
            file_name[i] = '?'

print("".join(file_name))

# ver1.
# input N, file name
N = int(input())
file_name_list =[]
for n in range(N):
    file_name_list.append(input())

search_same_name = list(file_name_list[0])

# compare
for n in range(N-1):
    file_name = list(file_name_list[n+1])
    str_length = len(search_same_name)
    for i in range(str_length):
        if search_same_name[i] != '?' and search_same_name[i] != file_name[i]:
            search_same_name[i] = '?'

print("".join(search_same_name))