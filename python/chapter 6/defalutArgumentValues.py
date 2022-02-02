def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Indian")
banner("INDIAN STAR","*")
banner(border='.',message="india")