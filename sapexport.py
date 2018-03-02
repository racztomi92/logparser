class Sapexportparser():
    @staticmethod
    def parse(data, connection):
        import datetime
        import re

        try:
            log_row = []
            f = open(data, 'r')
            # Inserting into database
            for line in f:
                if 'E:' in line:
                    log_row = line.split('[XML]')
                    if len(log_row) > 1:
                        log_row[0] = log_row[0][2:]
                        log_row[0] = log_row[0].replace('/', '-')
                        print('log_row 0: ' + log_row[0].strip() + '\n')
                        print('log_row 1: ' + log_row[1].strip() + '\n')

                        mydate = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                   int(log_row[0][1:3]), int(log_row[0][10:12]), int(log_row[0][13:15]),
                                                   int(log_row[0][16:18]))
                        insert = "INSERT INTO [ERROR_LOG] VALUES(TO_DATE('" + mydate2 + "' , '" + str(
                            log_row[1]) + next(f) + next(f) + next(f) + next(f) + "', 'SAP export', 'Error') "
                        print (insert)

                        c.execute(insert)
                        connection.commit()

                elif 'I:' in line:
                    log_row = line.split('[XML]')
                    log_row[0] = log_row[0][2:]
                    log_row[0] = log_row[0].replace('/', '-')
                    print('log_row 0: ' + log_row[0].strip() + '\n')
                    print('log_row 1: ' + log_row[1].strip() + '\n')
                    error = re.search('[eE][rR][rR][oO][rR]', log_row[1])
                    warning = re.search('[wW][aA][rR][nN][iI][nN][gG]', log_row[1])
                    if error is not None or warning is not None:
                        mydate2 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                    int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                    int(log_row[0][13:15]), int(log_row[0][16:18]))
                        insert2 = "INSERT INTO [LOG] VALUES(TO_DATE('" + mydate2 + "' , '" + str(
                            log_row[1]).strip().replace('\'', ' ') + "', 'SAP export', 'Warning') "

                        print(insert2)
                        c.execute(insert2)
                        connection.commit()

                    else:
                        mydate2 = datetime.datetime(int(log_row[0][7:9]) + 2000, int(log_row[0][4:6]),
                                                    int(log_row[0][1:3]), int(log_row[0][10:12]),
                                                    int(log_row[0][13:15]), int(log_row[0][16:18]))
                        insert2 = "INSERT INTO [LOG] VALUES(TO_DATE('" + mydate2 + "' , '" + str(
                            log_row[1]).strip().replace('\'', ' ') + "', 'SAP export' 'Info') "

                        print(insert2)
                        c.execute(insert2)
                        connection.commit()
                else:
                    print(line)

            return True
        except:
            return False
        finally:
            f.close()