def bubblesort(ns):
    def ordered(ns):
        for i in range(len(ns)-1):
            if ns[i] > ns[i+1]:
                return False
        return True
    while not ordered(ns):
        for i in range(len(ns)-1):
            if ns[i] > ns[i+1]:
                temp = ns[i+1]
                ns[i+1] = ns[i]
                ns[i] = temp