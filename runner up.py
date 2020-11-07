if __name__ == '__main__':
    N=int(input())
    list=list(set(map(int,input().strip().split(" "))))
    list.sort(reverse=True)
    print(f"{list[1]}")
