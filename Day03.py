subjucts = "    python, data structure, database    "
print(len(subjucts))
print(subjucts.strip())
print(subjucts.find("data"), subjucts.index("data"))
print(subjucts.find("dadfea")) #-1으로 return
#print(subjucts.index("dsfadasfda")) #error로 return
print(subjucts.rfind("data")) #뒤에서부터 찾는다
print(subjucts.count("data")) #단어가 몇개인지 센다
print(subjucts.center(40)) #문자 정렬 center,ljust,rjust가 있다
blurt = "what the fuck...?!"
print(blurt.strip("!?."))
print(blurt.capitalize()) #앞글자만 대문자
print(blurt.title()) #첫글자는 다 대문자
print(blurt.upper()) #모든글자 대문자
print(blurt.lower()) #모든글자 소문자