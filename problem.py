
def main():
    file = open('p:tmp\words.txt', 'r')
    content = file.read()
    token_list = content.split()
    Wlist = {}
    for x in token_list:
        if x in Wlist:
            Wlist[x] = Wlist[x] + 1
        else:
            Wlist[x] = 1
    print(Wlist)
    file.close
    

if __name__ == "__main__":
    main()