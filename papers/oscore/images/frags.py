import json
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# reads a json file
def read_json(path):
    with open(path, 'r') as myfile:
        return json.load(myfile)

data = read_json("fragmentation/fragmentation.json")
payloads = data["payloads"]
coap_len = data["coap"]["len"]
coap_frags = data["coap"]["frags"]
dtls_len = data["dtls"]["len"]
dtls_frags = data["dtls"]["frags"]
oscore_len = data["oscore"]["len"]
oscore_frags = data["oscore"]["frags"]

#make data look nicer with paralell lines
offset = 0.05
coap_frags = [x - offset for x in coap_frags]
dtls_frags= [x + offset for x in dtls_frags]
#oscore_frags = [x - offset for x in oscore_frags]

df_len = pd.DataFrame({'payload': payloads, 'COAP': coap_len, 'COAPS': dtls_len, 'OSCORE': oscore_len})
df_frags = pd.DataFrame({'payload': payloads, 'COAP': coap_frags, 'COAPS': dtls_frags, 'OSCORE': oscore_frags})


#fig, (ax1, ax2) = plt.subplots(2,1)
plt.figure(figsize=(4,2))
plt.plot( 'payload', 'COAPS', data=df_frags, color='maroon', marker='o')
plt.plot( 'payload', 'OSCORE', data=df_frags, color='navy', marker='s')
plt.plot( 'payload', 'COAP', data=df_frags, color='darkgray', marker='P', linestyle='dashed')
plt.xticks(payloads)
plt.yticks([1,2,3])
plt.xlabel('Payload size (Bytes)')
plt.ylabel('Packages per message')
#ax = plt.gca()
#ax.set_aspect(20)
plt.legend(loc='upper left')
plt.savefig("frags.png")
#plt.show()
