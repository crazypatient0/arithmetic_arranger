import arithmetic_arranger

def run_count(list,*args):
    a = arithmetic_arranger.arithmetic_arranger(list,*args)
    a.count()

if __name__ == '__main__':
    run_count(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)


