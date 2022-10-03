# num = list(range(1, 101))
# print(type(num))

# for i in range(len(num)):
# 	print(num[i], end=' ')
	
corona = "세븐틴 호시가 장꾸미를 발산했다. 최근 호시는 자신의 인스타그램을 통해 하트 이모티콘과 함께 사진을 게재했다. 공개된 사진 속 호시의 넓직한 어깨가 시선을 사로 잡았다. 또 비니를 착용하고 눈웃음을 짓고 있어 귀여운 매력을 발산했다. 한편 세븐틴이 16일 신곡 ‘_월드(_WORLD)’의 뮤직비디오 2차 티저를 공개했다."

corona = corona.replace('\n', '')
word = input('찾고자하는 단어를 입력하세요 : ')
print(f'{word}는 {corona.count(word)} 번 나옴')

sentence = corona.split('.')
for st in sentence :
	print(st)