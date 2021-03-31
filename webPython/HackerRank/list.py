# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    ans = []
    for i in range(0, N):
        a = input().split()
        if (a[0] == 'insert'):
            ans.insert(int(a[1]), int(a[2]))
        elif(a[0] == 'append'):
            ans.append(int(a[1]))
        elif(a[0] == 'remove'):
            ans.remove(int(a[1]))
        elif(a[0] == 'pop'):
            ans.pop()
        elif(a[0] == 'sort'):
            ans = sorted(ans)
        elif(a[0] == 'reverse'):
            ans = ans[::-1]
        else:
            print(ans)