# ------------------------------------------
#         Importing modules
# ------------------------------------------

import base64
import json
import os
import datetime
import pypyodbc

# ------------------------------------------
#         Reading config file
# ------------------------------------------

file_path = os.path.join(os.path.dirname(__file__), "data.txt")

data = json.load(open(file_path))

now = datetime.datetime.now()  # The current date

driver = data['driver']
server = data['server']
database = data['database']
user = data['uid']
password = data['password']
encoded_pwd = base64.b64decode(password)

# ------------------------------------------
#   !!!!!      Database connection     !!!!
# ------------------------------------------

connection = pypyodbc.connect('Driver={' + driver + '};'
                                                    'Server=' + server + ';'
                                                                         'Database=' + database + ';'
                                                                                                  'uid=' + user + ';pwd=' + encoded_pwd)
c = connection.cursor()

# --------------------------------------------
#   !!!!!   Reading data of log files    !!!!
# --------------------------------------------

xmlimport = data['xmlimport']
xmlimport_path = data['xmlimport_path']
xmlimport_destination = data['xmlimport_destination'] + '\\xmlimport' + str(now.year) + str(now.month) + str(
    now.day) + str(now.hour) + str(now.minute) + '.txt'
sapexport = data['sapexport']
sapexport_path = data['sapexport_path']
sapexport_destination = data['sapexport_destination'] + '\\sapexport' + str(now.year) + str(now.month) + str(
    now.day) + str(now.hour) + str(now.minute) + '.txt'
ppmimport = data['ppmimport']
ppmimport_path = data['ppmimport_path']
ppmimport_destination = data['ppmimport_destination'] + '\\ppmimport' + str(now.year) + str(now.month) + str(
    now.day) + str(now.hour) + str(now.minute) + '.txt'
batpath = data['batpath']
batdestination = data['batdestination']+'\\bat' + str(now.year) + str(now.month) + str(
    now.day) + str(now.hour) + str(now.minute) + '.txt'
mssqlupdate_path = data['mssqlupdate_path']
mssqlupdate_destination = data['mssqlupdate_destination']+'\\mssql_update' + str(now.year) + str(now.month) + str(
    now.day) + str(now.hour) + str(now.minute) + '.txt'
oracleinsert_path = data['oracleinsert_path']
oracleinsert_destination = data['oracleinsert_destination']+'\\oracle_insert' + str(now.year) + str(now.month) + str(
    now.day) + str(now.hour) + str(now.minute) + '.txt'



# ------------------------------------------------------
#   !!!!!      Importing sapexport's logparser     !!!!
# ------------------------------------------------------

from parsers.sapexport import Sapexportparser

result = Sapexportparser.parse(sapexport_path, connection)
if result == False:
    print "Error: You do not have log from sapexport"
elif result == True:
    os.rename(sapexport_path, sapexport_destination)
    open(sapexport_path, 'w')

# ------------------------------------------------------
#   !!!!!      Importing xmlimport's logparser     !!!!
# ------------------------------------------------------

from parsers.xmlimport import XMLimportparser

result = XMLimportparser.parse(xmlimport_path, connection)
if result == False:
    print "Error: You do not have log from xmlimport"
elif result == True:
    os.rename(xmlimport_path, xmlimport_destination)
    open(xmlimport_path, 'w')

# ------------------------------------------------------
#   !!!!!      Importing ppmimport's logparser     !!!!
# ------------------------------------------------------

from parsers.ppmimport  import PPMimportparser

result = PPMimportparser.parse(ppmimport_path, connection)
if result == False:
    print "Error: You do not have log from ppmimport"
elif result == True:
    os.rename(ppmimport_path, ppmimport_destination)
    open(ppmimport_path, 'w')

# ------------------------------------------------------
#   !!!!!      Importing bat's logparser     !!!!
# ------------------------------------------------------

from  parsers.batparser import BATexportparser

result = BATexportparser.parse(batpath, connection)
if result == False:
    print "Error: You do not have log from batexport"
elif result == True:
    os.rename(batpath,  batdestination)
    open(batpath, 'w')

# ------------------------------------------------------
#   !!!!!      Importing mssql update's logparser     !!!!
# -----------------------------------------------------

from parsers.mssqlupdate import Mssqlparser

result = Mssqlparser.parse(mssqlupdate_path, connection)
if result == False:
    print "Error: You do not have log from mssql update"
elif result == True:
    os.rename(mssqlupdate_path, mssqlupdate_destination)
    open(mssqlupdate_path, 'w')

# ------------------------------------------------------
#   !!!!!      Importing Oracle insert's logparser     !!!!
# -----------------------------------------------------

from parsers.oracleimport import OracleImportParser

result = OracleImportParser.parse(oracleinsert_path, connection)
if result == False:
    print "Error: You do not have log from mssql update"
elif result == True:
    os.rename(oracleinsert_path, oracleinsert_destination)
    open(oracleinsert_path, 'w')

connection.close()