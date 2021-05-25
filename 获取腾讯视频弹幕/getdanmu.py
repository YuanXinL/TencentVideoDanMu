import re
str = input("输入需要获取的网址：")
tag = re.findall(r"\/(.{11})\.", str)[0]
import requests
header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}
urls = "http://bullet.video.qq.com/fcgi-bin/target/regist?otype=json&vid=" + tag
res = requests.get(url = urls, headers=header)
res.encoding = "utf-8"
print("targetid获取结果:",res.text)
text = res.text
targetid = re.findall(r"(?<=\=)\w+", text)[1]
tagurl = "http://mfm.video.qq.com/danmu?timestamp=0&target_id=" + targetid
res = requests.get(url = tagurl, headers=header)
res.encoding = "utf-8"
import json
reques = json.loads(res.text)
danmu = reques['comments']
myinfo = open(targetid+'recode.md', mode = 'w',encoding='utf-8')
a = 0
for i in danmu:
    print("---",i['content'],"---" ,file=myinfo)
    a+=1
myinfo.seek(0,0)
print ("------输出成功！共",a,"条弹幕-----", file=myinfo)
myinfo.close()

