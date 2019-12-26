from kafka import KafkaConsumer, TopicPartition
import time, sys

SERVER='localhost:9092'
TOPIC='test1'
CLIENT_ID='py-1'
grp1 = sys.argv[1]
grp2 = sys.argv[2]

c1 = KafkaConsumer(
	  bootstrap_servers=[SERVER]
	, group_id=grp1
	, client_id=CLIENT_ID
	, auto_offset_reset='earlist'
	, enable_auto_commit=False)
c2 = KafkaConsumer(
	  bootstrap_servers=[SERVER]
	, group_id=grp2
	, client_id=CLIENT_ID
	, auto_offset_reset='earlist'
	, enable_auto_commit=False
	, max_poll_records=1)

offsets={}

for p in c1.partitions_for_topic(TOPIC):
    tp = TopicPartition(TOPIC, p)
    c1.assign([tp])
    beginning = list(c1.beginning_offsets([tp]).values())[0]
    committed = c1.committed(tp)
    end = list(c1.end_offsets([tp]).values())[0]
    position = c1.position(tp)
    print("partition: %s beginning: %s committed: %s end: %s position: %s" % 
		(p, beginning, committed, end, position))
    offsets[p] = position

tps2 = []
for p in c2.partitions_for_topic(TOPIC):
    tp = TopicPartition(TOPIC, p)
    tps2.append(tp)

c2.assign(tps2)

for tp in tps2:
	beginning = list(c2.beginning_offsets([tp]).values())[0]
	committed = c2.committed(tp)
	end = list(c2.end_offsets([tp]).values())[0]
	c2.seek(tp, offsets[tp[1]])
	position = c2.position(tp)
	print("partition: %s beginning: %s committed: %s end: %s position: %s" % 
		(tp[1], beginning, committed, end, position))
	c2.commit()

c1.close()
c2.close()
