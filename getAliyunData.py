#!usr/bin/env python
# coding:utf-8


import json
import urllib2



url = "https://yunlook-crawler.oss-cn-beijing.aliyuncs.com/test/libing/20180810/jobid_qq_video_ad_2018-08-10_14-31-12_12707_qq_item_172.16.16.8-10.20.40.4-7228-20180810-develop_1cceb50f51a63225d88aadcf2cf6240bjobid_qq_video_ad_2018-08-10_14-31-12_12707-video_ad-qq.json?Expires=1533889132&OSSAccessKeyId=TMP.AQHJcu_wFjtXJmXDiFYnvcdLEMZdNISwS3AGDKEbidMlWFtfa0SF95z7lEVNADAtAhUAqjxpJX3NQwAKOznkXSevRLAznCQCFC5U-gcXXTNV8CpqkresHAnz5D_Q&Signature=T%2B%2F8c9rvRjOGpIudA0P0sGxRQLA%3D"

read = urllib2.urlopen(url).readlines()


print "抓取{}条".format(len(read))
for i in read:
	i = json.loads(i,encoding='utf8')
	print json.dumps(i,ensure_ascii=False)
