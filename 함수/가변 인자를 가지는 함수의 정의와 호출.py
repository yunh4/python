def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
	print(f"이름 : {name}\t나이 : {age}\t".format(name, age), end=" ")
	print(lang1, lang2, lang3, lang4, lang5)
	
profile("구윤하", 17, "C", "Python", "Java", "C#")
profile("권순영", 27, "JS", "CSS", "Python", "", "")