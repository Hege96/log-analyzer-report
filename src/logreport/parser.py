import re
from datetime import datetime
from typing import Optional, Dict

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<ts>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<url>\S+) (?P<proto>[^"]+)" '
    r'(?P<status>\d{3}) (?P<bytes>\S+) '
    r'"(?P<ref>[^"]*)" "(?P<ua>[^"]*)"'
)

def parse_line(line):
    m=LOG_PATTERN.match(line)
    print(m)
