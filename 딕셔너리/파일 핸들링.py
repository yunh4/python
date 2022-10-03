#구글 드라이브 마운트
from google.colab import drive 
drive.mount('/content/gdrive/')
fp = open('/content/gdrive/My Drive/지역평균기온.txt', 'r', encoding='utf-8')
data = fp.read()
fp.close()
print(data)