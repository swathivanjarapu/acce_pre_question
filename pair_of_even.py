from asyncio import base_events


t=int(input())
for _ in range(t):
    a,b =map(int,input().split())
    aeven=a//2
    aodd=a-aeven
    beven=b//2
    bodd=b-beven
    ans=(aeven*beven)+(aodd*bodd)
    print(ans)


