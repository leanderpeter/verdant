
import pymongo
import sys

try:
  client = pymongo.MongoClient("Cluster, database, etc")
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# use database named "stocksTest"
db = client.stocksTest

# use a collection named "stocks"
my_collection = db["stocks"]

result = my_collection.find()

my_choice = ['TSLA', 'NIO']
endpoint = []

if result:
	# print(type(result))
	for i in result:
		for stock in my_choice:
			if i['stock_name'] == stock:
				endpoint.append(i)
			else:
				pass

for depots in endpoint:
	print(depots['portfolio_name'])
	for choice in my_choice:
		