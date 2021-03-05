players = ["황의조", "황희찬", "구자철", "이재성", "기성용"]

print("현재 경기 중인 선수 : ")
for i in range(0,len(players)):
    print(players[i])

outNum = input("OUT 시킬 선수 번호:")
inplayer = input("IN 할 선수 이름:")
outNum = int(outNum)

del players[outNum]
players.append(inplayer)

print("교체 결과 : ")
for i in range(0,len(players)):
    print(players[i])