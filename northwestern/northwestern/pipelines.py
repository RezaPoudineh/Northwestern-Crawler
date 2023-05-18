# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
from scrapy import item
from phpserialize import serialize, unserialize
from phpserialize import *
import json
import requests

def wp_insert_faculty( faculty_info ):
    url = 'https://applyallacademy.com/wp-admin/admin-ajax.php'
    faculty_info['research_area'] = json.dumps(faculty_info['research_area'])
    faculty_info['image'] = requests.utils.unquote(faculty_info['image'])
    myobj = {
        'action': 'add_faculty_api',
        'user': 'api_user',
        'pass': '7JThqMFBeMdYVHT',
        'faculty_info': json.dumps(faculty_info)
    }
    result = requests.post(url, data = myobj)
    return result

class NorthwesternPipeline:
        def __init__(self):
            self.create_connection()
        def create_connection(self):
            self.conn = mysql.connector.connect(
                host = '82.180.138.1',
                user = 'u319315404_hMsIA',
                passwd = 'Math1984@',
                db = 'u319315404_Jtej4'
        )
            self.curr = self.conn.cursor()
        def process_item(self, item, spider):
            self.stroe_db(item)
            return item
        
        def stroe_db(self,item):
            #reserch_area = ','.join(item["reserch_area"]).rstrip()
            # reserch_area_json = json.dumps(reserch_area)

            # x = wp_insert_faculty(faculty_info)
            # self.curr.execute(""" insert into wp_apply_faculty (image,name,title,email,program_id,school_id,research_area,link,creator_id)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            #               (
            #                   item['image'],
            #                   item['name'],
            #                   item['title'],
            #                   item['email'],
            #                   16,
            #                   110,
            #                   dumps(item['reserch_area']),
            #                   item['link'],
            #                   1
            #               ))
            # self.conn.commit()
            
            faculty_info = {
                'name': item['name'],
                'title': item['title'],
                'email': item['email'],
                'program_id': item['program_id'],
                'school_id': item['school_id'],
                'research_area': item['research_area'],
                'link': item['link'],
                'department': '',
                'department_link': '',
                'google_scholar': '',
                'image': item['image']
            }
            wp_insert_faculty(faculty_info)



# class NorthwesternPipeline:
#     def process_item(self, item, spider):
#         return item
