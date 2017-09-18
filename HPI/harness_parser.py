import csv
import json
import pandas as pd
from backend.connect_db import *
from backend.models import *


def harness_parser(filename,create_time):
    file_create_date =create_time
    success_msg = 'SUCCESS'
    session = get_session()
    conn = create_conn()

    if filename.endswith('.csv'):
        try:
            harness_data = pd.read_csv(filename)
            harness_data['created_date'] = file_create_date
            with conn:
                harness_data.to_sql('users',conn,if_exists='append',index=False)
            pf = ParsedFile(filename=filename,file_created_date=file_create_date,parse_success=True,
                               parse_message=success_msg)
        except StandardError as err:
            err_type = err.__class__.__name__
            pf = ParsedFile(filename=filename, file_created_date=file_create_date, parse_success=False,
                            parse_message='{} : {}'.format(err_type,err.message))
    elif filename.endswith('.txt'):
        try:
            with open(filename,'r') as fl:
                file_data = json.loads(fl.read().strip())
            fl.close()
            harness_data = pd.DataFrame(file_data)
            harness_data['created_date'] = file_create_date
            with conn:
                harness_data.to_sql('users', conn, if_exists='append', index=False)
            pf = ParsedFile(filename=filename, file_created_date=file_create_date, parse_success=True,
                        parse_message=success_msg)
        except ValueError as err:
            try:
                with open(filename,'r') as fl:
                    dialect = csv.Sniffer().sniff(fl.read(),delimiters=',;\t')
                    fl.seek(0)
                    all_rows = [row for row in csv.reader(fl,dialect)]
                fl.close()
                dict_keys = all_rows[0]
                file_data = [dict(zip(dict_keys,val)) for val in all_rows[1:] ]
                harness_data = pd.DataFrame(file_data)
                harness_data['created_date'] = file_create_date
                with conn:
                    harness_data.to_sql('users', conn, if_exists='append', index=False)
                pf = ParsedFile(filename=filename, file_created_date=file_create_date, parse_success=True,
                            parse_message=success_msg)
            except StandardError as err:
                err_type = err.__class__.__name__
                pf = ParsedFile(filename=filename, file_created_date=file_create_date, parse_success=False,
                                parse_message='{} : {}'.format(err_type, err.message))
        except StandardError as err:
            err_type = err.__class__.__name__
            pf = ParsedFile(filename=filename, file_created_date=file_create_date, parse_success=False,
                    parse_message='{} : {}'.format(err_type, err.message))
    else:
        pf = ParsedFile(filename=filename, file_created_date=file_create_date, parse_success=False,
                        parse_message="Unknown file type")
    session.add(pf)
    session.commit()
