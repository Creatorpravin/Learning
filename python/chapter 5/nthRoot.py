def nthRoot(radicand, n):
    return radicand ** (1/n)

def ordinalSuffic(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'

def ordinal(value):
    return str(value) + ordinalSuffic(value)

def displayNthRoot(radicand,n):
    root = nthRoot(radicand,n)
    message =  'The ' + ordinal(n) + ' root of ' + str(radicand)+' is ' +str(root)
    print(message)

displayNthRoot(64, 8)