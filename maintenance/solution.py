def solution(x):
    result = sorted(x, key=lambda x:[int(i) for i in x.split('.')])
    return result