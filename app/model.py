from eql.utils import stream_stdin_events, stream_file_events
from eqllib import normalization, main, loader
from eql import parse_query, EqlError
import sys

class CreateQuery():
    def __init__(self, input_file, input_type):
        self.config = loader.Configuration.default_with_analytics()
        self.input_file = input_file
        self.input_type = input_type
        self.results = list()

    def parse(self, text):
        try:
            return parse_query(text, implied_base=True, implied_any=True)
        except EqlError as exc:
            print(exc, file=sys.stderr)
            sys.exit(2)
        
    def run_query(self, query_str):
        # Define data source
        data_source = self.input_type

        # Normalize the data
        source = self.config.normalizers[data_source]

        # Generate query
        query = self.parse(query_str)

        query = self.config.normalizers[source.domain].normalize_ast(query)

        events = stream_file_events(self.input_file, None, None)

        engine = normalization.NormalizedEngine({'print': True})
        engine.add_query(query)
        engine.stream_events(source.data_normalizer(e) for e in events)