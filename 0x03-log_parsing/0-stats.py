#!/usr/bin/python3

"""
Log Parsing
"""

import sys
import re
import signal

status_codes = {
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


def main():
    """
    main: parses a log to analyse it
    """

    pattern = r'((\d*\.?){1,3}){4} - \[(\d*\-?){3} (\d*:?){3}\.\d*\] "GET /projects/260 HTTP/1\.1" \d{3} \d{1,4}'

    count_logs = 0

    for line in sys.stdin:
        match = re.match(pattern, line)

        if match:
            values = get_code_and_size(line.split(" ")[-2:], status_codes)
            count_logs += 1 if True else 0

            if count_logs == 10:
                print_status_codes(status_codes)
                reset_status_codes(status_codes)
                count_logs = 0
                pass
            # print(f"{line}")


def get_code_and_size(splited, status_codes):
    """
    get_code_and_size: gets the split and stores the rep into the status_code object

    splited (List): holds the status code and file size
    status_code (dict): holds the status code
    """

    for i in range(2):
        if i == 0:
            try:
                converted_status = int(splited[i])
                status_codes[converted_status] += 1
            except TypeError:
                return False
        else:
            try:
                converted_size = int(splited[i].split("\n")[0])
                status_codes["file_size"] += converted_size
            except TypeError:
                return False
    return True


def reset_status_codes(status_codes):
    """
    reset_status_codes: resets all the status code

    status_code (dict): the code and number of times recorded
    """

    for k, v in status_codes.items():
        if v != 0:
            status_codes[k] = 0


def print_status_codes(status_codes):
    """
    print_status_code: print the status code

    status_code (dict): prints the status code
    """

    file_size = status_codes["file_size"]
    print(f"File size: {file_size}")

    for k, v in status_codes.items():
        if v != 0 and k != "file_size":
            print(f"{k}: {v}")


def handler(signum, frame):
    print_status_codes(status_codes)
    raise KeyboardInterrupt


signal.signal(signal.SIGINT, handler)


if __name__ == "__main__":
    main()
