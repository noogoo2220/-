# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('Tlqkf', color="#c8ffc8")
image background1 = "제목 없음"
image bg2= "나여"
image c1="dd"
# 여기에서부터 게임이 시작합니다.
label start:
    scene background1
    show c1
    e "ㅆ발"
    "나" "왜 욕하고 지랄이야"
    scene bg2
    e "Tqkffkfkfk" with vpunch
    
    return
