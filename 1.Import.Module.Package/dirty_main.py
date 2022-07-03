from application.salary import *
from application.db.people import *
import datetime
from dateutil import tz


LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

def getIsoTime():
	return datetime.datetime.now(tz=LOCAL_TIMEZONE).isoformat()

if __name__ == '__main__':
	print(f"Time: {getIsoTime()} ({LOCAL_TIMEZONE})")
	calculate_salary()
	get_employees()