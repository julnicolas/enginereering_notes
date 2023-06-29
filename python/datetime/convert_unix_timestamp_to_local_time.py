from datetime import datetime

# Test with epoch timestamp (-> int) as input
timestamp = datetime.timestamp(datetime.now())
t = datetime.fromtimestamp(timestamp)
print(t)
