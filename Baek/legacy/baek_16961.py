# # def input_values():
# N = int(input())
# reserved_list = []
# # map(func, iterable_data)
# for n in range(N):
#     reserved_list.append(list(input().split()))
#
# # define T, S, total
# t_list = []
# t_reserved_list = [0 for n in range(366)]
# s_list = []
# s_reserved_list = [0 for n in range(366)]
# total_list = []
# total_reserved_list = [0 for n in range(366)]
# long_day = 0
#
# # T 투숙일, S 투숙일, 총 투숙일 구하기
# for n in range(N):
#     t_s_classification = reserved_list[n][0]
#     temp_list = [int(reserved_list[n][1]), int(reserved_list[n][2])]
#     if t_s_classification == 'T':
#         t_list.append(temp_list)
#     else:
#         s_list.append(temp_list)
#     total_list.append(temp_list)
#     long_day = max(long_day, total_list[n][1] - total_list[n][0])
#
# t_list.sort()
# s_list.sort()
# total_list.sort()
#
#
# def calculate_total_reserved_num(_list, _reserved_list):
#     for n in range(len(_list)):
#         for i in range(366):
#             start_day = _list[n][0] - 1
#             end_day = _list[n][1] - 1
#             if start_day <= i <= end_day:
#                 _reserved_list[i] += 1
#     return _reserved_list
#
#
# t_reserved_list = calculate_total_reserved_num(t_list, t_reserved_list)
# s_reserved_list = calculate_total_reserved_num(s_list, s_reserved_list)
# total_reserved_list = calculate_total_reserved_num(total_list, total_reserved_list)
#
# reserved_date = 0  # 1
# max_people_num = max(total_reserved_list)  # 2
# non_fight_date = 0  # 3
# non_fight_date_list = [0 for i in range(366)]  # 4
#
# for i in range(366):
#     if total_reserved_list[i] > 0:
#         reserved_date += 1
#     if t_reserved_list[i] != s_reserved_list[i] or t_reserved_list[i] == 0 or s_reserved_list[i] == 0:
#         pass
#     else:
#         non_fight_date += 1
#         non_fight_date_list[i] = total_reserved_list[i]
# not_reserved_date = 366 - reserved_date
#
# print(reserved_date)
# print(max_people_num)
# print(non_fight_date)
# print(max(non_fight_date_list))
# print(max(long_day)+1)

N = int(input())
reserved_total_num_1 = 0
max_reserved_num_2 = 0
non_fight_day_3 = 0
non_fight_day_max_num_4 = 0
long_day_5 = 0
cnt_reserved_list = [[0 for m in range(2)] for n in range(366)]
for n in range(N):
     reserved_list = list(input().split())
     start_day = int(reserved_list[1]) - 1
     end_day = int(reserved_list[2])
     t_s_classification = reserved_list[0]
     for i in range(start_day, end_day):
          if t_s_classification == 'T':
               cnt_reserved_list[i][0] += 1
          else:
               cnt_reserved_list[i][1] += 1
     long_day_5 = max(long_day_5, end_day - start_day)

for i in range(366):
     reserved_num = cnt_reserved_list[i][0] + cnt_reserved_list[i][1]
     if reserved_num > 0:
          reserved_total_num_1 += 1
     max_reserved_num_2 = max(max_reserved_num_2, reserved_num)
     if reserved_num > 0 and cnt_reserved_list[i][0] == cnt_reserved_list[i][1]:
          non_fight_day_3 += 1
          non_fight_day_max_num_4 = max(non_fight_day_max_num_4, reserved_num);

print(reserved_total_num_1)
print(max_reserved_num_2)
print(non_fight_day_3)
print(non_fight_day_max_num_4)
print(long_day_5)