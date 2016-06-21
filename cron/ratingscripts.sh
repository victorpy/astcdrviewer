#!/bin/bash

/usr/bin/php /usr/src/cdrviewer/cdrviewer/cron/ratecdr.php >> /var/log/ratecdr.log 2>&1
/usr/bin/php /usr/src/cdrviewer/cdrviewer/cron/rateincomingcdr.php >> /var/log/rateincomingcdr.log 2>&1
