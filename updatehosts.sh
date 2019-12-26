if [ "$1" == "" ]; then
  echo usage updatehosts.sh [IP NAME]
  echo exam updatehosts.sh 1.2.3.4 test.com
  exit
fi

BAKUPDIR=/BACKUP/hosts
mkdir -p $BAKUPDIR \
  && cp /etc/hosts $BAKUPDIR/hosts.`date '+%Y%m%d_%H%M'`

if [ $? -ne 0 ]; then
  echo error while backing up original file
  exit
fi

cat /etc/hosts | sed "s/^\([^#].*$2\)$/#\1\n$1	$2/" |tee /tmp/hosts.new \
  && cp /tmp/hosts.new /etc/hosts
