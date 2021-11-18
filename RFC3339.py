import datetime

d = datetime.datetime.utcnow()
end_time = (d.isoformat('T')+ 'Z')

d2 = d+datetime.timedelta(days=-1)
start_time = (d2.isoformat('T')+ "Z")

