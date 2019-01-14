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

## Convert BRO logs keys

Version `0.6.2` of EQL does not parse BRO keys with dots like `id.orig_h` or `id.orig_p`

1. Mac OSX sed:
    1. `sed -i '' 's:id\.orig_h:dest_addr:g' *.jsonl`
    1. `sed -i '' 's:id\.orig_p:dest_port:g' *.jsonl`
    1. `sed -i '' 's:id\.resp_h:src_addr:g' *.jsonl`
    1. `sed -i '' 's:id\.resp_p:src_port:g' *.jsonl`
1. Linux sed:
    1. `sed -i 's:id\.orig_h:dest_addr:g' *.jsonl`
    1. `sed -i 's:id\.orig_p:dest_port:g' *.jsonl`
    1. `sed -i 's:id\.resp_h:src_addr:g' *.jsonl`
    1. `sed -i 's:id\.resp_p:src_port:g' *.jsonl`

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
    1. `eqllib query -s "Bro events" -f dns.jsonl "bro_dns where true | unique"`
    1. ![EQL DNS unique queries](.img/eql_dns_query.png)

## Resources/Sources

* [Github - EQL](https://github.com/endgameinc/eql)
* [Github - EQLLIB](https://github.com/endgameinc/eqllib)
* [ReadTheDocs - EQLLIB - Schema](https://eqllib.readthedocs.io/en/latest/schemas.html#)
* [ReadTheDocs - EQLLIB - Command line](https://eql.readthedocs.io/en/latest/cli.html)
* [Github - EQLLIB - Sysmon source config](https://github.com/endgameinc/eqllib/blob/master/eqllib/sources/sysmon.toml)
* [ReadTheDocs - EQLLIB - Pipes](https://eql.readthedocs.io/en/latest/query-guide/pipes.html#unique)