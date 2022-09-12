이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('dd', color="#c8ffc8")


# 여기에서부터 게임이 시작합니다.
label start:

    "학교가자"
    "충돌"
    menu 충돌:
        "한마디"
        "Choice 1":
            "ㄴㄴ"
            "ㅇ"
            jump next1
        "Choice 2":
            
            "ㄴ"
            jump bad

    return

label bad:
    "ㅁㅎ"
    return

label next1:
    menu:
        "한마디"
        "ㅌ1":
         "1"
           
        "ㅌ2":
            "ㅌ1"
           
            jump bad
    return    
