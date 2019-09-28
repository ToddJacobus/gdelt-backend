import json, sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_date_ranges():
    # Create ranges, 1 month in breadth,
    # from 2018-01-01 to 2019-01-01
    dates = []
    for i in range(12):
        date_string = "2018-{}-01".format(i+1)
        dates.append(date_string)
    # Get that last one for 2019...
    dates.append('2019-01-01')
    return dates

def write_sql_for(dates):
    sql = []
    sql_indexes = []
    table_list = [
        'gkg_sources',
        'gkg_counts',
        'gkg_images',
        'gkg_liwc',
        'gkg_locations',
        'gkg_orgs',
        'gkg_people',
        'gkg_themes'
    ]
    for table in table_list:
        for i, date_string in enumerate(dates):
            if i == len(dates) - 1:
                break
            else:
                year = date_string.split('-')[0]
                month = date_string.split('-')[1]
                next_date = dates[i+1]
                sql.append(
                """
                    CREATE TABLE IF NOT EXISTS data.{table}_yr{year}m{month}
                        PARTITION OF data.{table}
                            FOR VALUES FROM ('{date_string}') TO ('{next_date}');
                """.format(
                    table = table,
                    year = year,
                    month = month,
                    date_string = date_string,
                    next_date = next_date
                ))

                sql_indexes.append(
                    """
                    CREATE INDEX IF NOT EXISTS {table}{year}_{month}_pub_date_idx ON data.{table}_yr{year}m{month} USING btree (pub_date);  
                    """.format(
                        table = table,
                        year = year,
                        month = month,
                    )
                )
    sql_single = " ".join(sql)
    index_sql_single = " ".join(sql_indexes)
    return sql, sql_single, index_sql_single

def create_the_tables_for(Session, sql_list, single_transaction=False):
    count = 1
    total = len(sql_list)
    session = Session()
    if single_transaction:
        try:
            session.execute(single_transaction)
        except:
            raise
        finally:
            session.close()
    else:
        for sql in sql_list:
            try:
                sys.stdout.write("\rCreating table {} of {}...".format(count, total))
                sys.stdout.flush()
                import pdb; pdb.set_trace()
                session.execute(sql)
            except:
                raise
            finally:
                session.close()
                count+=1

## -- HELPER FUNCTIONS ---------------------------------------------------------

def getDbParams(params_path):
    # input path to json file holding database parameters
    # Return dictionary of params.
    with open(params_path, 'r') as file:
        params = json.load(file)
    return params

## -- GLOBALS ------------------------------------------------------------------
db_credentials_path = r"../../gkg_master_credentials.json" # Scombrini local
params = getDbParams(db_credentials_path)
engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(params['username'],params['password'],params['host'],params['port'],params['database_name']))
Session = sessionmaker(bind=engine)

# Write out SQL for creating tables.
# I think it's easier to just save this as a .sql file
# and run it in psql or PGAdmin.
sql_list, create_tables, create_indexes = write_sql_for(create_date_ranges())
import pdb; pdb.set_trace()
with open('create_indexes.sql', 'w+') as file:
    file.write(create_indexes)
