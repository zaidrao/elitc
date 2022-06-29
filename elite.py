import platform
b = platform.architecture()[0]
if b == '64bit':
    import elite
elif b == '32bit':
    print("32bit NOT SUPPORTED")