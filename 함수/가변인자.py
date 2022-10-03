def profile(name, age, *language) :
	print(f"이름 : {name}\t나이 : {age}\t".format(name, age), end=" ")
	for lang in language : #튜플
		print(lang, end=" ")
	print()
	
profile("구윤하", 17, "C", "Python", "Java", "C#")
profile("권순영", 27, "JS", "CSS", "Python")