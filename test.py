import datetime
import time

now = datetime.datetime.utcnow()
time.sleep(2)
b = datetime.datetime.utcnow()

print(int((b - now).total_seconds()) > 1)

# if int((now.Subtract(self.timer)).total_seconds()) > self.timeout_period:
# return True
# else:
# return False
