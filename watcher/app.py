import logging
from datetime import datetime
import watchtower
import json


root = logging.getLogger()
if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s ~ %(app_name)s ~  %(start_time)s ~ %(end_time)s ~ %(no_of_records)s ~ %(status)s ~ %(job_type)s ~ %(message)s', level = logging.INFO)
logger = logging.getLogger("testlogger1")       
logger.addHandler(watchtower.CloudWatchLogHandler(log_group="/aws/watchtowerlogger",stream_name="testlogger1"+datetime.now().strftime("%Y%m%d%H%M%S")))
extra = {"app_name":"testjob", "module_name":"", "start_time":datetime.now().strftime("%Y%m%d %H%M%S"), "end_time":"", "no_of_records":"100", "status":"running", "job_type": "full"  }
logger.info(extra, extra=extra)