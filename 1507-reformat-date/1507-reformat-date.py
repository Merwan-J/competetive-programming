class Solution:
	def reformatDate(self, date: str) -> str:

		list_date = date.split()  

		d = {"Jan" : '01', "Feb": '02'
			 , "Mar": '03', "Apr": '04'
			 , "May": '05', "Jun": '06'
			 , "Jul": '07', "Aug": '08'
			 , "Sep": '09', "Oct": '10'
			 , "Nov": '11', "Dec": '12'}

		day = list_date[0].replace("th","").replace("nd","").replace("st","").replace("rd","")
		month = list_date[1]
		year = list_date[2]

		if int(day) < 10:
			day = '0'+day

		res = year + '-' + d[month] + '-' + day
		return res