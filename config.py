import json
import os
import base64
from pprint import pprint

# ------------------------------------------
#         Make object with global variables
# ------------------------------------------

class Config(object):
    driver = ''
    server = ''
    database = ''
    uid = ''
    password = ''
    xmlimport_path = ''
    xmlimport_destination = ''
    sapexport_path = ''
    sapexport_destination = ''
    ppmimport_path = ''
    ppmimport_destination = ''
    batpath = ''
    batdestination = ''
    mssqlupdate_path = ''
    mssqlupdate_destination = ''
    oracleinsert_path = ''
    oracleinsert_destination = ''

    # The class "constructor" - It's actually an initializer

    def __init__(self):
        self.driver = raw_input('Enter the type of the driver:')
        self.server = raw_input('Enter the IP address of the server:')
        self.database = raw_input('Enter the database name:')
        self.uid = raw_input('Enter the user name:')
        password = raw_input('Enter the password:')
        self.encoded_password = base64.b64encode(password.encode())

        # self.configurate()

    # -------------------------------
    #        Requesting user input
    # -------------------------------

    def configurate(self):
        while True:
            source = raw_input(
                'Enter the source of your logs (xmlimport, sapexport, ppmimport, batch, mssqlupdate, exit(if no more source)):')
            if source == 'xmlimport':
                self.xmlimport_path = raw_input(
                    'Enter the path for the log file(\'drive:\\folder\\folder\\file_name.txt\'): ')
                self.xmlimport_destination = raw_input(
                    'Enter the path to the destination where the file will be placed (\'drive:\\folder\\folder\\file_name.txt\'): ')
            elif source == 'sapexport':
                self.sapexport_path = raw_input(
                    'Enter the path for the log file(\'drive:\\folder\\folder\\file_name.txt\'): ')
                self.sapexport_destination = raw_input(
                    'Enter the path to the destination where the file will be placed (\'drive:\\folder\\folder\\file_name.txt\'): ')
            elif source == 'ppmimport':
                self.ppmimport_path = raw_input(
                    'Enter the path for the log file(\'drive:\\folder\\folder\\file_name.txt\'): ')
                self.ppmimport_destination = raw_input(
                    'Enter the path to the destination where the file will be placed (\'drive:\\folder\\folder\\file_name.txt\'): ')
            elif source == 'batch':
                self.batpath = raw_input('Enter the path for the log file(\'drive:\\folder\\folder\\file_name.txt\'): ')
                self.batdestination = raw_input(
                    'Enter the path to the destination where the file will be placed (\'drive:\\folder\\folder\\file_name.txt\'): ')
            elif source == 'mssqlupdate':
                self.mssqlupdate_path = raw_input(
                    'Enter the path for the log file(\'drive:\\folder\\folder\\file_name.txt\'): ')
                self.mssqlupdate_destination = raw_input(
                    'Enter the path to the destination where the file will be placed (\'drive:\\folder\\folder\\file_name.txt\'): ')
            elif source == 'oracleinsert':
                self.oracleinsert_path = raw_input(
                    'Enter the path for the log file(\'drive:\\folder\\folder\\file_name.txt\'): ')
                self.oracleinsert_destination = raw_input(
                    'Enter the path to the destination where the file will be placed (\'drive:\\folder\\folder\\file_name.txt\'): ')
            elif source == 'exit':
                break
            else:
                print('This programm can\'t handle this kind of log file')

        print('The configuration is completed')


# -------------------------------
#        Serialize
# -------------------------------


configData = Config()
configData.configurate()

#                                                                    |\            ________
# ---------------------------------------------             -----    | |          |\       /|
#        Transform to JSON and write to a file             | O O |   | |   -----> | \_____/ |
# ---------------------------------------------            | .:. | __|_|__        |_________|
#                                                           -----    |_|

s = json.dumps(configData.__dict__)  # s set to: input
# Deserialize
clones = json.loads(s)
print clones

file_path = os.path.join(os.path.dirname(__file__), 'data.json')  # path is the same as where this file located
with open(file_path, 'wb') as outfile:  # write binary
    outfile.truncate()
    # outfile.write(json.dumps(clones))
    pprint(clones, outfile)

