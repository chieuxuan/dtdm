a = input('Nhập vào họ tên:')
nam_sinh = int(input('Nhập vào năm sinh:'))
#hiển thị kết quả:
import datetime
year = datetime.datetime.now().year
tuoi = year - nam_sinh
print('Bạn \"', a.upper(), '\"năm nay', tuoi, 'tuổi!')
