import sys
import re
in_file_user = open(sys.argv[1],"r")
lines_user=in_file_user.readlines()
in_file_user.close()
num_lines=len(lines_user)

for i in range(num_lines):
 	lines_user[i]=lines_user[i].rstrip("\n")
 	xx=lines_user[i]
 	lines_user[i]=re.sub(r"([:|;|])([-|=]?)([L|)|(|P|p|D)])", r' \1\2\3 ', lines_user[i])
 	# line = re.sub('((https?://)?([\w-]+\.)?[\w-][\w-]+(\.co)?\.[a-z-]{2,4}(/[^\s\"\'\(\)]+)*(/|(\?[^\s\"\'\(\)]+))?)([^\w])', ' \\1 \\8', line) # this is for urls
 	#Date Handling 
 	while re.search(r'[\s]+([\d]{2,4})[/|.|-]([\d]{2})[/|.|-]([\d]{2,4})[\s]+',lines_user[i]):
		mt=re.search(r'[\s]+([\d]{2,4})[/|.|-]([\d]{2})[/|.|-]([\d]{2,4})[\s]+',lines_user[i])
		ap=' CSL772:^~~^:'
		month=mt.group(1)
		date=mt.group(2)
		year=mt.group(3)
		if len(mt.group(1))<=2 and int(mt.group(1))>12:
			date=mt.group(1)
			month=mt.group(2)
			year=mt.group(3)
		elif len(mt.group(2))<=2 and int(mt.group(2))>12:
			date=mt.group(2)
			month=mt.group(1)
			year=mt.group(3)
		if len(mt.group(1))==4:
			year=mt.group(1)
			month=mt.group(2)
			date=mt.group(3)
		if len(date)==1:
			date='0'+date
		if len(month)==1:
			month='0'+month			
		ap1=int(year)
		
		if len(year)<4:
			if ap1>20:
				ap1=-100
			ap1=2000+int(year)
		lines_user[i]=re.sub(mt.group(), ap+str(ap1)+"^~^"+month+"^~^"+date+" ", lines_user[i])
	month_map={"jan":"01","january":"01","feb":"02","february":"02","mar":"03","march":"03","apr":"04","april":"04","may":"05","june":"06","july":"07","aug":"08","august":"08","sep":"09","sept":"09","september":"09","oct":"10","october":"10","nov":"11","november":"11","dec":"12","december":"12"}
	flag=True
	while flag and re.search(r'[\s]+([\d]{1,2})(th)?(rd)?(st?) ([a-z]+)[\s]*[.,]?([\d]{2,4})?[\s]+|$',lines_user[i],re.I):
		mt=re.search(r'[\s]+([\d]{1,2})(th)?(rd)?(st)? ([a-z]+)[\s]*[.,]?([\d]{2,4})?[\s|.|,]+|$',lines_user[i],re.I)
		try:
			date=mt.group(1)
			year=mt.group(6)
			mon=str(mt.group(5)).lower()

		
			mon=month_map[mon]
			if len(date)==1:
				date="0"+date
			if len(year)<4:
				ap=0
				if int(year)>20:
					ap=-100
				year=str(2000+int(year)+ap)
			lines_user[i]=re.sub(mt.group()," CSL772:^~~^:"+year+"^~^"+mon+"^~^"+date+" ",lines_user[i])
		except:
			flag=False
			pass
	flag=True
	while flag and re.search(r'[\s]+([a-z]+)[\s]+([\d]{1,2})(th)?(rd)?(st)?[\s]*[.,]?([\d]{2,4})?[\s]+|$',lines_user[i],re.I):
		mt=re.search(r'[\s]+([a-z]+)[\s]+([\d]{1,2})(th)?(rd)?(st)?[\s]*[.,]?([\d]{2,4})?[\s]+|$',lines_user[i],re.I)
		try:
			date=mt.group(2)
			year=mt.group(6)
			mon=str(mt.group(1)).lower()
		
			mon=month_map[mon]
			if len(date)==1:
				date="0"+date
			if len(year)<4:
				ap=0
				if int(year)>20:
					ap=-100
				year=str(2000+int(year)+ap)
			lines_user[i]=re.sub(mt.group()," CSL772:^~~^:"+year+"^~^"+mon+"^~^"+date+" ",lines_user[i])
		except:
			flag=False
			pass
	flag=True
	while flag and re.search(r"[\s]+([a-z]+)[\s]*[.,']?([\d]{2,4})[\s]+|$",lines_user[i],re.I):
		mt=re.search(r"[\s]+([a-z]+)[\s]*[.,']?([\d]{2,4})[\s]+|$",lines_user[i],re.I)
		try:
			year=mt.group(2)
			mon=str(mt.group(1)).lower()
			mon=month_map[mon]
			if len(year)<4:
				ap=0
				if int(year)>20:
					ap=-100
				year=str(2000+int(year)+ap)
			lines_user[i]=re.sub(mt.group()," CSL772:^~~^:"+year+"^~^"+mon+" ",lines_user[i])
		except:
			flag=False
			pass
	# while re.search(r"[\s]+([a-z]+)[\s]+",lines_user[i],re.I):
	# 	try:
	# 		mt=re.search(r"[\s]+([a-z]+)[\s]+",lines_user[i],re.I)
	# 		mon=month_map[str(mt.group(1))]
	# 		lines_user[i]=re.sub(mt.group()," CSL772:^~~^:"+"^%^"+"^~^"+mon+" ",lines_user[i])
	# 	except:
	# 		lines_user[i]=re.sub(mt.group()," ^^"+mt.group(1)+"^^ ",lines_user[i])
	# 		pass

	#Punctuation Handling
 	lines_user[i]=re.sub(r'([\w]+)([>|*|-|;|"|.|,|(|:|)|?|!]+)([\s|$|-|;|"|.|,|(|:|)|?|!]+|$)', r'\1 \2\3', lines_user[i])
 	# lines_user[i]=re.sub(r'([\w]+)([-|;|"|.|,|(|:|)|?|!]+)([\s|$|-|;|"|.|,|(|:|)|?|!]+|$)', r'\1 \2\3', lines_user[i])

 	lines_user[i]=re.sub(r'([\w]+)([#]+)(.)', r'\1 \2\3', lines_user[i])
 	lines_user[i]=re.sub(r'[.]([\w]+) ([.])', r'.\1.', lines_user[i])
 	lines_user[i]=re.sub(r'([\w]+)([;|"|,|(|)|!]+)([\w]+)', r'\1 \2 \3', lines_user[i])
 	lines_user[i]=re.sub(r'([\w]+)([-]+)([#]?[\w]+)', r'\1 \2\3', lines_user[i])
 	# lines_user[i]=re.sub(r'([\w]+)([.])([\w]+)', r'\1 \2 \3', lines_user[i])
 	# lines_user[i]=re.sub(r'//([\w]+) ([.]) ([\w]+)([/|.])', r'//\1\2\3\4', lines_user[i])	
 	lines_user[i]=re.sub(r'([\w]+)([,]+)([\w]+)', r'\1 \2 \3', lines_user[i])
 	lines_user[i]=re.sub(r'([\w]+)([.]{2,})([\w]+)', r'\1 \2 \3', lines_user[i])
 	# lines_user[i]=re.sub(r'([\w])(@)([\w]+)', r'\1 \2\3', lines_user[i])
 	lines_user[i]=re.sub(r'(@)([,])', r'\1 \2', lines_user[i])	
 	lines_user[i]=re.sub(r'(RT)(@)([\w]+)', r'\1 \2\3', lines_user[i])
 	lines_user[i]=re.sub(r'([a-z]+)([:])([a-z]+)', r'\1 \2 \3', lines_user[i],re.I)
 	lines_user[i]=re.sub(r'([-|.|,|(|)|?|!]+)(["]+)', r'\1 \2', lines_user[i])
 	lines_user[i]=re.sub(r'([)|(|#]+)([&|!|"|)|()]+)', r'\1 \2', lines_user[i])
 	lines_user[i]=re.sub(r'^([(|*|"]+)([\w]+)', r'\1 \2', lines_user[i])

 	lines_user[i]=re.sub(r"^([']+)([\w]+)", r'\1 \2', lines_user[i])
 	
 	# lines_user[i]=re.sub(r'([^\d]+)([:]+)([^\d]+)', r'\1 \2 \3', lines_user[i])
 	lines_user[i]=re.sub(r'()([!|"|)]+)([\w|.|,]+)', r'\1\2 \3', lines_user[i])
 	# lines_user[i]=re.sub(r'[$]([\d]+)', r'[$] \1', lines_user[i])
 	lines_user[i]=re.sub(r'([\s]+)([*|&|"|.|,|(|)|?|!]+)([\w]+|[)|(])', r'\1\2 \3', lines_user[i])
 	lines_user[i]=re.sub(r"([\w]+)([']+)([\s|$]+|$)", r'\1 \2\3', lines_user[i])
 	# lines_user[i]=re.sub(r"([\w]+)([']+)([\w]+)", r'\1 \2 \3', lines_user[i])
 	lines_user[i]=re.sub(r"([,|(|)|?|!]+)([']+)", r'\1 \2', lines_user[i])
 	lines_user[i]=re.sub(r"([)]+)([:|.]+)", r'\1 \2', lines_user[i])
 	lines_user[i]=re.sub(r"([']+)([,|(|)|?|!]+)", r'\1 \2', lines_user[i])
 	lines_user[i]=re.sub(r"([\s]+)([']+)([\w]+)", r'\1\2 \3', lines_user[i])
 	#Clitics Handling
 	lines_user[i]=re.sub(r"([\w]+)([']+)m", r'\1 am', lines_user[i])
 	lines_user[i]=re.sub(r"([\s]+)(I)(m)([\s]+)", r'\1\2 am\4', lines_user[i])
 	lines_user[i]=re.sub(r"([\s]+)(I)(M)([\s]+)", r'\1\2 AM\4', lines_user[i])
 	lines_user[i]=re.sub(r"([\s]+)(i)(m)([\s]+)", r'\1\2 am\4', lines_user[i])
 	lines_user[i]=re.sub(r' couldnt ',r' could not ',lines_user[i])
 	lines_user[i]=re.sub(r' dont ',r' do not ',lines_user[i])
 	lines_user[i]=re.sub(r' wont ',r' would not ',lines_user[i])
 	lines_user[i]=re.sub(r' whos ',r' who is ',lines_user[i])
 	lines_user[i]=re.sub(r' Whos ',r' Who is ',lines_user[i])
 	lines_user[i]=re.sub(r" y'all ",r' you all ',lines_user[i])
 	lines_user[i]=re.sub(r"([\w]+)([']+)d", r'\1 would', lines_user[i])
 	lines_user[i]=re.sub(r"([\w]+)n([']+)t", r'\1 not', lines_user[i])
 	lines_user[i]=re.sub(r"([\w]+)([']+)t", r'\1 not', lines_user[i])
 	lines_user[i]=re.sub(r"([\w]+)([']+)ve", r'\1 have', lines_user[i])
 	lines_user[i]=re.sub(r"([\w]+)([']+)re", r'\1 are', lines_user[i])
	lines_user[i]=re.sub(r"([\w]+)([']+)ll", r'\1 will', lines_user[i])	
 	# lines_user[i]=re.sub(r"([\w]+)([']+)s", r"\1 's", lines_user[i])
 	lines_user[i]=re.sub(r"([\w]+)([']+)s", r"\1 is", lines_user[i])
 	lines_user[i]=re.sub(r"([\w]+)(['])([\s]+)", r"\1 's\3", lines_user[i])
 	# lines_user[i]=re.sub(r"@([\d]+)", r"@ \1", lines_user[i])
 	#smileys
 	
 	lines_user[i]=re.sub(r'(\w+)([.])($)', r'\1 \2\3', lines_user[i])
 	#Time handling
 	while re.search(r'[\s]+([\d]{1,2})[:|.]([\d]{1,2})[\s]*p[.]?m[.]?',lines_user[i],re.I):
		mt=re.search(r'[\s]+([\d]{1,2})[:|.]([\d]{1,2})[\s]*p[.]?m[.]?',lines_user[i],re.I)
		lines_user[i]=re.sub(mt.group(), ' CSL772:T:'+str((int(mt.group(1))+12)*100+int(mt.group(2))), lines_user[i])
	while re.search(r'[\s]+([\d]{1,2})[:|.]([\d]{1,2})[\s]*a[.]?m[.]?',lines_user[i],re.I):
		mt=re.search(r'[\s]+([\d]{1,2})[:|.]([\d]{1,2})[\s]*a[.]?m[.]?',lines_user[i],re.I)
		if int(mt.group(1))<10:
			ap=' CSL772:T:0'
		else:
			ap=' CSL772:T:'
		xxx=int(mt.group(1))
		if xxx==12:
			xxx=0
		lines_user[i]=re.sub(mt.group(), ap+str((xxx)*100+int(mt.group(2))), lines_user[i])
 	while re.search(r'[\s]+([\d]{1,2})[\s]*p[.]?m[.]?[\s]*([\w]*[\s]?[\w]*)',lines_user[i],re.I):
		mt=re.search(r'[\s]+([\d]{1,2})[\s]*p[.]?m[.]?[\s]*([\w]*[\s]?[\w]*)',lines_user[i],re.I)
		ap1=" "
		if mt.group(2)=="Eastern":
			ap1=":EST "
		elif mt.group(2)=="Indian Time" or mt.group(2)=="IST":
			ap1=":IST "
		elif mt.group(2)=="California Time":
			ap1=":CST "
		elif mt.group(2)=="London":
			ap1=":GMT "
		xxx=int(mt.group(1))
		if xxx==12:
			xxx=0
		lines_user[i]=re.sub(mt.group(), ' CSL772:T:'+str(xxx+12)+'00'+ap1, lines_user[i])
	while re.search(r' ([\d]{1,2})[\s]*a[.]?m[.]?[\s]*([\w]*[\s]?[\w]*)',lines_user[i],re.I):
		mt=re.search(r' ([\d]{1,2})[\s]*a[.]?m[.]?[\s]*([\w]*[\s]?[\w]*)',lines_user[i],re.I)
		ap1=" "
		if mt.group(2)=="Eastern" or mt.group(2)=="Eastern Time":
			ap1=":EST "
		elif mt.group(2)=="Indian Time" or mt.group(2)=="IST":
			ap1=":IST "
		elif mt.group(2)=="California Time" or mt.group(2)=="California":
			ap1=":PST "
		elif mt.group(2)=="London" or mt.group(2)=="London Time":
			ap1=":GMT "
		if int(mt.group(1))<10:
			ap=' CSL772:T:0'
		else:
			ap=' CSL772:T:'
		lines_user[i]=re.sub(mt.group(), ap+str(int(mt.group(1)))+'00'+ap1, lines_user[i])
	#just Year Handling
	while re.search(r'[\s]+((19)|(20))([\d]{2})[\s]+',lines_user[i],re.I):
		mt=re.search(r'[\s]+((19)|(20))([\d]{2})[\s]+',lines_user[i],re.I)
		ap=' CSL772:^~~^:'
		lines_user[i]=re.sub(mt.group(), ap+mt.group(1)+mt.group(4)+" ", lines_user[i])
	#time handling without specified am/pm
	while re.search(r'([\s]+)([\d]{1,2})[:]([\d]{1,2})[\s]+',lines_user[i],re.I):
		mt=re.search(r'([\s]+)([\d]{1,2})[:]([\d]{1,2})[\s]+',lines_user[i],re.I)
		if int(mt.group(2))<10:
			ap='CSL772:T:0'
		else:
			ap='CSL772:T:'
		lines_user[i]=re.sub(mt.group(), mt.group(1)+" "+ap+str(int(mt.group(2))*100 + int(mt.group(3)))+'|'+str((int(mt.group(2))+12)*100 + int(mt.group(3)))+" ", lines_user[i])
	#intermediates used removed	
	lines_user[i]=re.sub(r'\^%\^',r'????',lines_user[i])
	lines_user[i]=re.sub(r'\^~~\^',r'D',lines_user[i])
	lines_user[i]=re.sub(r'\^~\^',r'-',lines_user[i])
 	token=lines_user[i].split()
 	print xx
 	print len(token)
	for j in range(len(token)):
		print token[j]
		