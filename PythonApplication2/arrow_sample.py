import arrow

utc = arrow.utcnow()
utc = utc.replace(hours=-3)
local = utc.to('US/Pacific')

print(local.humanize())
