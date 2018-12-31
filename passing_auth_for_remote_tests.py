
#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import sys, os
import splunklib.client as client

HOST = "localhost"
PORT = "8089"
USERNAME = "admin"
PASSWORD = "changeme"

# original auth for remote testing
service = client.connect(
        host=HOST,
        port=PORT,
        username=USERNAME,
        password=PASSWORD,
        owner='nobody')

# verify access
kv_client = service.kvstore
for kv in kv_client:
    print(kv)

## note: attempts to pass the token caused tuple errors, possible bug in Splunklib 
# save the cookie
my_cookie = service.get_cookies()

# logout
service.logout()

# THIS SHOULD ERROR, proves you are logged out
kv_client = service.kvstore
for kv in kv_client:
    print(kv)
# AuthenticationError: Request aborted: not logged in.

# new login with cookie
service = client.connect(
        host=HOST,
        port=PORT,
        cookie=my_cookie,
        owner='nobody')

# verify access in new session
kv_client = service.kvstore
for kv in kv_client:
    print(kv)




