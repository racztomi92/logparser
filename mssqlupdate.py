class Mssqlparser():
    @staticmethod
    def parse(data, connection):
        import re

        try:
            raw_lines = []
            lines = []
            f = open(data, 'r')
            for line in f:
                raw_lines.append(line)

            pattern = re.compile("[0-9]{2}[/.-][0-9]{2}[/.-][0-9]{4}")

            for line in f:
                if pattern.match(line[:39]):
                    raw_lines[index - 1] += raw_lines[index]
                    del raw_lines[index]

            for line in raw_lines:
                line = line.replace('\n', ' ')
                line = line.replace("'", "''")
                lines.append(line)
            for line in lines:
                time = line[0:39]
                log_message = line[39:]
                error = re.search('[eE][rR][rR][oO][rR]', log_message)
                warning = re.search('[wW][aA][rR][nN][iI][nN][gG]', log_message)
                if error is not None:
                    insert = "INSERT INTO [LOG] VALUES (TO_DATE('" + time + "', 'yyyy.MM.dd HH24:MI:ss'), '" + log_message + "', 'MSSQL upgrade', 'Info') "

                    c.execute(insert)
                    c.execute("COMMIT")
                    c.close()

                elif warning is not None:
                    insert = "INSERT INTO [LOG] VALUES (TO_DATE('" + time + "', 'yyyy.MM.dd HH24:MI:ss'), '" + log_message + "', 'MSSQL upgrade', 'Warning') "
                    c.execute(insert)
                    c.execute("COMMIT")
                    c.close()

                else:
                    insert = "INSERT INTO [LOG] VALUES (TO_DATE('" + time + "', 'yyyy.MM.dd HH24:MI:ss'), '" + log_message + "', 'MSSQL upgrade', 'Warning') "
                    c.execute(insert)
                    c.execute("COMMIT")
                    c.close()
            return True
        except:
            return False
        finally:
            f.close()