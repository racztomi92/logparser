class BATexportparser():
    @staticmethod
    def parse(data, connection):
        try:
            import re

            raw_lines = []
            lines = []
            data = open(batpath, 'r')
            for line in data:
                raw_lines.append(line)

            def new_row():
                pattern = re.compile("[0-9]{4}[/.-][0-9]{1,2}[/.-][0-9]{1,2}")
                print pattern
                for line in f:
                    if pattern.match(line[:10]):
                        raw_lines[index - 1] += raw_lines[index]
                        del raw_lines[index]
                        new_row()

            new_row()

            for line in raw_lines:
                line = line.replace('\n', ' ')
                line = line.replace("'", "''")
                lines.append(line)

                for line in lines:
                    time = line[0:19]
                    log_message = line[20:]
                    error = re.search('[eE][rR][rR][oO][rR]', log_message)
                    warning = re.search('[wW][aA][rR][nN][iI][nN][gG]', log_message)
                    if error is not None:
                        insert = "INSERT INTO LOG (DATUM, UZENET) VALUES (TO_DATE('" + time + "', 'yyyy.MM.dd HH24:MI:ss'), '" + log_message + "', 'bat export', 'Error') "
                        # print (insert)
                        c.execute(insert)
                        c.execute("COMMIT")
                    elif warning is not None:
                        insert = "INSERT INTO LOG (DATUM, UZENET) VALUES (TO_DATE('" + time + "', 'yyyy.MM.dd HH24:MI:ss'), '" + log_message + "', 'bat export', 'Warning') "
                        # print (insert)
                        c.execute(insert)
                        c.execute("COMMIT")
                    else:
                        insert = "INSERT INTO LOG (DATUM, UZENET) VALUES (TO_DATE('" + time + "', 'yyyy.MM.dd HH24:MI:ss'), '" + log_message + "', 'bat export', 'Info') "
                        # print (insert)
                        c.execute(insert)
                        c.execute("COMMIT")

                c.close()
            return True
        except:
            return False
        finally:
            f.close()