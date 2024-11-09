#!/usr/bin/python3

"""
Log Parsing
"""

import sys
import re
import signal

status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
    "file_size": 0,
}

line_count = 0


def parse_line(line):
    """
    Parses a single line of log and
    updates status_counts based on the status code and file size
    """

    pattern = (
        r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )
    match = re.match(pattern, line)

    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        status_counts["file_size"] += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1


def print_stats():
    """
    Prints the current statistics: total file size
    and count of each status code
    """
    if status_counts["file_size"]:
        print(f"File size: {status_counts['file_size']}")
    for code in sorted(
        k for k in status_counts if isinstance(k, int) and status_counts[k] > 0
    ):
        print(f"{code}: {status_counts[code]}")


def reset_stats():
    """
    Resets status counts except for the total file size
    """

    for code in status_counts:
        if isinstance(code, int):
            status_counts[code] = 0


def signal_handler(signum, frame):
    """
    Signal handler to print statistics on keyboard interrupt
    """

    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


for line in sys.stdin:
    parse_line(line)

    line_count += 1

    if line_count % 10 == 0:
        print_stats()

if line_count % 10 != 0:
    print_stats()
