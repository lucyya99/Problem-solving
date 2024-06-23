# N = int(input())
# palindrome_str = list(input()) # 나중에 ''.join(palindrome_str)으로 문자열로 만들어 줄 예정
# if N & 1 == 1:
#     N_half = (N + 1) // 2
# else:
#     N_half = N // 2
# N -= 1
# for n in range(N_half):
#     if palindrome_str[n] == '?':
#         if palindrome_str[N-n] == '?':
#             palindrome_str[n] = palindrome_str[N-n] = 'a'
#         else:
#             palindrome_str[n] = palindrome_str[N-n]
#     else:
#         palindrome_str[N - n] = palindrome_str[n]
#
# print("".join(palindrome_str))

N = int(input())
palindrome_str = list(input()) # 나중에 ''.join(palindrome_str)으로 문자열로 만들어 줄 예정
if N & 1 != 0:
    N_half = (N + 1) // 2
else:
    N_half = N // 2
for n in range(N_half):
#     print(f'{n} : {palindrome_str[n]}, {-1-n} : {palindrome_str[-1-n]}')
    if palindrome_str[n] == '?':
        if palindrome_str[-1-n] == '?':
            palindrome_str[n] = palindrome_str[-1-n] = 'a'
        else:
            palindrome_str[n] = palindrome_str[-1-n]
    else:
        palindrome_str[-1-n] = palindrome_str[n]

print("".join(palindrome_str))