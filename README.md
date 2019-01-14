# ThreatHuntingEQLandBro

## Install/Setup EQL and EQLLUB

## EQL

1. `pip install eql`
1. `python seutp.py install`
1. `cp bro-schema.json <python2.7 base_dir>/site-packages/eql/etc/schema.json`
    1. Over write default schema
    1. `<python2.7 base_dir>` - `/usr/local/lib/python2.7` on Mac OSX

### EQLLIB

1. `git clone https://github.com/endgameinc/eqllib.git`
1. `cd eqllib`
1. `python setup.py install`
1. `cp bro-domain.toml <python2.7 base_dir>/site-packages/eqllib-*.egg/eqllib/domains/bro-domain.toml`
1. `cp bro-source.toml <python2.7 base_dir>/site-packages/eqllib-*.egg/eqllib/sources/bro.toml`

## Example Queries

1. `cd example_logs conn.jsonl`
1. Check if new schema, BRO domain, and BRO source are working
    1. `eqllib query -s "Bro events" -f conn.jsonl "bro_conn where true"`
    1. ![EQL connection list](.img/eql_conn_list.png)
1. Count the connections in the conn.log
    1. `eqllib query -s "Bro events" -f conn.jsonl "bro_conn where true | count"`
    1. ![EQL connection count](.img/eql_conn_count.png)
1. Count the connections with a destination IP addr
    1. `eqllib query -s "Bro events" -f conn.jsonl "bro_conn where destination_address == '8.8.8.8' | count"`
1. Unique DNS queries
    1. `eqllib query -s "Bro events" -f dns.jsonl "bro_dns where query == '*' | unique"`

## Resources/Sources

* [Github - EQL](https://github.com/endgameinc/eql)
* [Github - EQLLIB](https://github.com/endgameinc/eqllib)
* [ReadTheDocs - EQLLIB - Schema](https://eqllib.readthedocs.io/en/latest/schemas.html#)
* [Github - EQLLIB - Sysmon source config](https://github.com/endgameinc/eqllib/blob/master/eqllib/sources/sysmon.toml)