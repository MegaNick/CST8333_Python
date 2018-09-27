class Tuna():
    def __init__(self, id, name, valuew):
        self.id = id
        self.name = name
        self.value = valuew

    id = 0
    name = ""
    value = ""


class main ():
    print("Test classs!!!")
    list = []
    setset = set(list)

    for count in range (0,4):
        print("Counter-",count)
        x = Tuna(count, "Test", "Test")
        list.append(x)



    for x in setset:
        print(x.id, x.name, x.value)




if __name__ == '__main__': main()