class PPMimportparser():
    @staticmethod
    def parse(data, connection):
        import datetime
        import re

        try:
            log_row = []
            f = open(data, 'r')
            with open(ppmimport_path, 'r') as f:
                for line in f:
                    if 'E:' in line:
                        if '[IMP]' in line:
                            log_row = line.split('[IMP]')
                            if len(log_row) > 1:
                                log_row[0] = log_row[0][2:]
                                log_row[0] = log_row[0].replace('/', '-')
                                print('E')
                                print(line)
                                mydate = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                           int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                           int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert = "INSERT INTO [ERROR_LOG] VALUES('" + str(mydate) + "'" + ", '" + str(
                                    log_row[1]) + next(f) + next(f) + next(f) + next(f) + "', 'PPM import', 'Error') "
                                c.execute(insert)
                                connection.commit()
                        elif '[EIM]' in line:
                            log_row = line.split('[EIM]')
                            if len(log_row) > 1:
                                log_row[0] = log_row[0][2:]
                                log_row[0] = log_row[0].replace('/', '-')
                                print('E2')
                                print(line)
                                mydate = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                           int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                           int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert = "INSERT INTO [ERROR_LOG] VALUES('" + str(mydate) + "'" + ", '" + str(
                                    log_row[1]) + next(f) + next(f) + next(f) + next(f) + "', 'PPM import', 'Error') "
                                c.execute(insert)
                                connection.commit()
                        elif '[MGR]' in line:
                            log_row = line.split('[MGR]')
                            if len(log_row) > 1:
                                log_row[0] = log_row[0][2:]
                                log_row[0] = log_row[0].replace('/', '-')
                                print('E3')
                                print(line)
                                mydate = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                           int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                           int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert = "INSERT INTO [ERROR_LOG] VALUES('" + str(mydate) + "'" + ", '" + str(
                                    log_row[1]) + next(f) + next(f) + next(f) + next(f) + "', 'PPM import', 'Error') "
                                c.execute(insert)
                                connection.commit()
                        elif '[KIC]' in line:
                            log_row = line.split('[KIC]')
                            if len(log_row) > 1:
                                log_row[0] = log_row[0][2:]
                                log_row[0] = log_row[0].replace('/', '-')
                                print('E2')
                                print(line)
                                mydate = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                           int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                           int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert = "INSERT INTO [ERROR_LOG] VALUES('" + str(mydate) + "'" + ", '" + str(
                                    log_row[1]) + next(f) + next(f) + next(f) + next(f) + "', 'PPM import', 'Error') "
                                c.execute(insert)
                                connection.commit()
                        else:
                            print('Undefined condition or row between the rows of PPM error messages')
                    elif 'S:' in line:
                        if '[EIM]' in line:
                            log_row = line.split('[EIM]')
                            log_row[0] = log_row[0][2:]
                            log_row[0] = log_row[0].replace('/', '-')
                            print(1)
                            error = re.search('[eE][rR][rR][oO][rR]', log_row[1])
                            warning = re.search('[wW][aA][rR][nN][iI][nN][gG]', log_row[1])
                            if error is not None or warning is not None:
                                mydate2 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                            int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                            int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert2 = "INSERT INTO [LOG] VALUES('" + str(mydate2) + "'" + ", '" + str(
                                    log_row[1]).strip().replace('\'', ' ') + "', 'PPM import','Warning') "
                                c.execute(insert2)
                                connection.commit()

                            else:
                                mydate2 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                            int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                            int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert2 = "INSERT INTO [LOG] VALUES('" + str(mydate2) + "'" + ", '" + str(
                                    log_row[1]).strip().replace('\'', ' ') + "', 'PPM import', 'Info') "
                                c.execute(insert2)
                                connection.commit()
                        elif '[MGR]' in line:
                            log_row = line.split('[MGR]')
                            log_row[0] = log_row[0][2:]
                            log_row[0] = log_row[0].replace('/', '-')
                            print(3)
                            if 'error' or 'warning' in line:
                                mydate2 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                            int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                            int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert2 = "INSERT INTO [LOG] VALUES('" + str(mydate2) + "'" + ", '" + str(
                                    log_row[1]).strip().replace('\'', ' ') + "', 'PPM import','Warning') "
                                c.execute(insert2)
                                connection.commit()

                            else:
                                mydate3 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                            int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                            int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert3 = "INSERT INTO [LOG] VALUES('" + str(mydate3) + "'" + ", '" + str(
                                    log_row[1]).strip().replace('\'', ' ') + "', 'PPM import', 'Info') "
                                c.execute(insert3)
                                connection.commit()
                        elif '[IMP]' in line:
                            log_row = line.split('[IMP]')
                            log_row[0] = log_row[0][2:]
                            log_row[0] = log_row[0].replace('/', '-')
                            print(4)
                            error = re.search('[eE][rR][rR][oO][rR]', log_row[1])
                            warning = re.search('[wW][aA][rR][nN][iI][nN][gG]', log_row[1])
                            if error is not None or warning is not None:
                                mydate2 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                            int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                            int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert2 = "INSERT INTO [LOG] VALUES('" + str(mydate2) + "'" + ", '" + str(
                                    log_row[1]).strip().replace('\'', ' ') + "', 'PPM import','Warning') "
                                c.execute(insert2)
                                connection.commit()


                            else:
                                mydate4 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                            int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                            int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert4 = "INSERT INTO [LOG] VALUES('" + str(mydate4) + "'" + ", '" + str(
                                    log_row[1]).strip().replace('\'', ' ') + "', 'PPM import', 'Info') "
                                c.execute(insert4)
                                connection.commit()
                        elif '[KIC]' in line:
                            log_row = line.split('[KIC]')
                            log_row[0] = log_row[0][2:]
                            log_row[0] = log_row[0].replace('/', '-')
                            print(5)
                            if 'error' or 'warning' in line:
                                mydate2 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                            int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                            int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert2 = "INSERT INTO [LOG] VALUES('" + str(mydate2) + "'" + ", '" + str(
                                    log_row[1]).strip().replace('\'', ' ') + "', 'PPM import','Warning') "
                                c.execute(insert2)
                                connection.commit()

                            else:
                                mydate5 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                            int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                            int(log_row[0][13:15]), int(log_row[0][16:18]))
                                insert5 = "INSERT INTO [LOG] VALUES('" + str(mydate5) + "'" + ", '" + str(
                                    log_row[1]).strip().replace('\'', ' ') + "', 'PPM import', 'Info') "
                                c.execute(insert5)
                            connection.commit()
                        else:
                            print('Undefined condition or row between the rows of success PPM import')
                    else:
                        print('Undefined row type')
            return True
        except:
            return False
        finally:
            f.close()