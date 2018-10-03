class Tuna():
    def __init__(self, id, name, valuew):
        self.id = id
        self.name = name
        self.value = valuew

    id = 0
    name = ""
    value = ""


def main ():
    print("Test classs!!!")
    list = []
    setset = set(list)

    for count in range (0,4):
        print("Counter-",count)
        x = Tuna(count, "Test", "Test")
        list.append(x)

    for x in setset:
        print(x.id, x.name, x.value)

    a = ["apple", 'banana', 'orange']
    print(a)

    b = {'fruit': 'apple', 'fruit': 'orange', 'vegetable': 'potato', 'vegetable': 'tomato'}
    print(b.items())
    print(b.get('fruit'))

    c = {}
    def insertDic(key, word):
        temp = c.get(key)
        if temp == None:
            c.update({key: [word]})
        else:
            temp.append(word)
            c.update({key: temp})

    insertDic('car', 'red')
    insertDic('car', 'blue')
    insertDic('fruit', 'apple')
    insertDic('fruit', 'orange')
    insertDic('vegetable', 'potato')
    insertDic('vegetable', 'tomato')
    insertDic('vegetable', 'cucumber')

    print(c)





if __name__ == '__main__': main()