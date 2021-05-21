import time
import datetime


def checkTimeout(start: datetime, timeout_period: int) -> bool:
    # a = datetime.datetime.utcnow()
    # time.sleep(1)
    now = datetime.datetime.utcnow()
    if int((now - start).total_seconds()):
        return True
    else:
        return False
