#!usr/bin/env python
# coding:utf-8

import time
import sys
import traceback
from elasticsearch import Elasticsearch


from config.config import es_ip,es_port,es_user,es_pass


class EsUtils(object):

    def __init__(self, hosts=es_ip, port=es_port, http_auth=(es_user, es_pass)):
        self.es = Elasticsearch(hosts=hosts, port=port, http_auth=http_auth)


    def search(self, index, searchbody):
        try:
            resault = self.es.search(index = index, body = searchbody,size=10000)

            return resault
        except Exception as e:
            print traceback.format_exc(sys.exc_info())
            print e

    def search_scroll(self,index, searchbody, search_type="scan",scroll="1m"):

        resault = self.es.search(index=index, body=searchbody, search_type="scan", scroll="1m")
        scrollID = resault['_scroll_id']

        response = self.es.scroll(scroll_id=scrollID, scroll="1m")
        return  response
