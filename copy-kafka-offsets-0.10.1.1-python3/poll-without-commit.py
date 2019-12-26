from kafka import KafkaConsumer, TopicPartition
import time, sys

SERVER='localhost:9092'
TOPIC='test1'
CLIENT_ID='py-1'

grp1=sys.argv[1]
grp2=sys.argv[2]

c1 = KafkaConsumer(
	  TOPIC
	, bootstrap_servers=[SERVER]
	, group_id=grp1
	, client_id=CLIENT_ID
	, auto_offset_reset='earlist'
	, enable_auto_commit=False
	, max_poll_records=1)
c2 = KafkaConsumer(
	  TOPIC
	, bootstrap_servers=[SERVER]
	, group_id=grp2
	, client_id=CLIENT_ID
	, auto_offset_reset='earlist'
	, enable_auto_commit=False
	, max_poll_records=1)

'''
for msg in c1:
	print("%d:%d: key=%s value=%s" % (msg.partition, msg.offset, msg.key, msg.value[:60]))
	#time.sleep(3)
'''

while (True):
	try:
		rec1 = c1.poll()
		if(rec1 != {}):
			msg = list(rec1.values())[0][0]
			print("p:%d o:%d k:%s v:%s" % (msg.partition, msg.offset, msg.key, msg.value[:60]))
	except RuntimeError as e:
		print('error', e)
	try:
		rec2 = c2.poll()
		if(rec2 != {}):
			msg = list(rec2.values())[0][0]
			print("p:%d o:%d k:%s v:%s" % (msg.partition, msg.offset, msg.key, msg.value[:60]))
	except RuntimeError as e:
		print('error', e)
	time.sleep(2)

c1.close()
c2.close()

