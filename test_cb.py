from cloudburst.client.client import CloudburstConnection
local_cloud = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
cloud_sq = local_cloud.register(lambda _, x: x * x, 'square')
print(cloud_sq(2).get())
