import hashlib

# Encoded data
encoded = r'[{"__class__":"ServerRequest","requestData":[],"requestClass":"InventoryService","requestMethod":"getItems","requestId":18},{"__class__":"ServerRequest","requestData":[{"__class__":"LoadTimePerformance","module":"City","loadTime":11120}],"requestClass":"LogService","requestMethod":"logPerformanceMetrics","requestId":19}]'

# User key from json requests (h=XXXXXXXXX)
user_key = "U-xVyWkc8422nqPUQpSS1JMX"

# Secret from ForgeHX-xxxxxx.js, function "generateRequestPayloadSignature"
secret = "+q1IHuiGLlFNT+3SzQKJ5ZqZ5pn1akE+uFHA2oqEfTtM6RMlWzz9ZkW6a7hPLA0jcgaoX/fPT4V/Shmoy8ie/Q=="

data = (user_key + secret + encoded).encode('utf-8')

# This should be the same value you see for the 'Signature' header in the request
signature = hashlib.md5(data).hexdigest()[0:10]
print(signature)