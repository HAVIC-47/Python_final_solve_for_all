def sum_svg(*args):
    total= sum(args)
    avarage= total/len(args)
    return total, avarage

print(sum_svg(1,2,3,4,5))
print(sum_svg(1,2,3,4,5,6,7,8,9,10))