def get_summ(one, two, delimiter='&'):
    return str(one)+delimiter+str(two)

ans = get_summ('Learn', 'python')
print(ans)
print(ans.upper())
