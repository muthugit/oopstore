from oopstore import Client
oopstore_client = Client('/tmp')

my_text = 'mthu'
oopstore_client.save(key=123,obj=my_text)