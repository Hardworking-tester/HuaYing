# encoding:utf-8
# author:wwg
import uuid
print uuid.uuid1()
ui=str(uuid.uuid4())
print ui
print ui.replace('-','')
print type(ui)
str(uuid.uuid4()).replace('-','')