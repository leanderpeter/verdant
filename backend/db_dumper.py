
import pymongo
import sys


portfolio_documents = []

eingabe = None

while eingabe != 'exit':

	eingabe = input('Portfolio Name: ')
	if eingabe != 'exit':
		stock_name = input('Name der Aktie: ')
		wert = input('Anteil der Aktie: ')
		portfolio_documents.append({"portfolio_name": eingabe, "stock_name":stock_name, "share":float(wert)})
	else:
		pass

	
	print(portfolio_documents)



# Replace the placeholder data with your Atlas connection string. Be sure it includes
# a valid username and password! Note that in a production environment,
# you should not store your password in plain-text here.

try:
  client = pymongo.MongoClient("mongodb+srv://leander:Miaufertent1@cluster0.1fjme.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# use database named "stocksTest"
db = client.stocksTest

# use a collection named "stocks"
my_collection = db["stocks"]

# drop the collection in case it already exists
try:
	pass
#  my_collection.drop()


# return a friendly error if an authentication error is thrown
except pymongo.errors.OperationFailure:
  print("An authentication error was received. Are your username and password correct in your connection string?")
  sys.exit(1)
# INSERT DOCUMENTS
#
# You can insert individual documents using collection.insert_one().
# In this example, we're going to create four documents and then 
# insert them all with insert_many().

try: 
 result = my_collection.insert_many(portfolio_documents)

# return a friendly error if the operation fails
except pymongo.errors.OperationFailure:
  print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
  sys.exit(1)
else:
  inserted_count = len(result.inserted_ids)
  print("I inserted %x documents." %(inserted_count))

  print("\n")

# FIND DOCUMENTS
#
# Now that we have data in Atlas, we can read it. To retrieve all of
# the data in a collection, we call find() with an empty filter. 

result = my_collection.find()




