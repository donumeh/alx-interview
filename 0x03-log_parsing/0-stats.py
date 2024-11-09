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

    pattern = r'((\d*\.?){1,3}){4} - \[(\d*\-?){3} (\d*:?){3}\.\d*\] "GET /projects/260 HTTP/1\.1" \d{3} \d{1,4}'
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
    if line:
        parse_line(line)

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

if line_count % 10 != 0:
    print_stats()


# def main():
#     """
#     main: parses a log to analyse it
#     """

#     pattern = r'((\d*\.?){1,3}){4} - \[(\d*\-?){3} (\d*:?){3}\.\d*\] "GET /projects/260 HTTP/1\.1" \d{3} \d{1,4}'

#     count_logs = 0

#     for line in sys.stdin:
#         match = re.match(pattern, line)

#         if match:
#             values = get_code_and_size(line.split(" ")[-2:], status_codes)
#             count_logs += 1 if True else 0

#             if count_logs == 10:
#                 print_status_codes(status_codes)
#                 reset_status_codes(status_codes)
#                 count_logs = 0
#                 pass
#             # print(f"{line}")


# def get_code_and_size(splited, status_codes):
#     """
#     get_code_and_size: gets the split and stores the rep into the status_code object

#     splited (List): holds the status code and file size
#     status_code (dict): holds the status code
#     """

#     for i in range(2):
#         if i == 0:
#             try:
#                 converted_status = int(splited[i])
#                 status_codes[converted_status] += 1
#             except TypeError:
#                 return False
#         else:
#             try:
#                 converted_size = int(splited[i].split("\n")[0])
#                 status_codes["file_size"] += converted_size
#             except TypeError:
#                 return False
#     return True


# def reset_status_codes(status_codes):
#     """
#     reset_status_codes: resets all the status code

#     status_code (dict): the code and number of times recorded
#     """

#     for k, v in status_codes.items():
#         if v != 0:
#             status_codes[k] = 0


# def print_status_codes(status_codes):
#     """
#     print_status_code: print the status code

#     status_code (dict): prints the status code
#     """

#     file_size = status_codes["file_size"]
#     print(f"File size: {file_size}")

#     for k, v in status_codes.items():
#         if v != 0 and k != "file_size":
#             print(f"{k}: {v}")


# def handler(signum, frame):
#     print_status_codes(status_codes)
#     raise KeyboardInterrupt


# signal.signal(signal.SIGINT, handler)


# if __name__ == "__main__":
#     main()
