#!/usr/bin/python3
"""
Module defines main function which outputs summar of logs
"""
import sys


def main() -> None:
    """
    Function infinitely loops reading from stdin and parse to output.
    """
    stat_cod_dict = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0,
    }
    lines_count, tot_file_size = 0, 0

    try:
        for line in sys.stdin:
            if check_format(line):
                file_size = int(line.split(' ')[-1])
                stat_code = line.split(' ')[-2]
                tot_file_size += file_size
                stat_cod_dict[stat_code] += 1
                lines_count += 1
            if lines_count == 10 :
                output_summary(tot_file_size, stat_cod_dict)
                lines_count = 0
        output_summary(tot_file_size, stat_cod_dict)
    except (KeyboardInterrupt):
        output_summary(tot_file_size, stat_cod_dict)
    return None


def check_format(log: str) -> bool:
    """
    Verify single line log format
    """
    log_elms = log.split(' ')
    if len(log_elms) != 9:
        return False
    if log_elms[-1][:-1].isdigit() and log_elms[-2].isdigit():
        return True
    return False


def output_summary(tot_size: int, status_codes: dict) -> None:
    """Output to stdout summary of 10 log files

    Args:
        tot_size (int): Total byte size from beginning
        status_codes (dict): Status codes count dictionary

    Returns:
        None
    """
    sys.stdout.write('File size: {}\n'.format(tot_size))
    for code, count in status_codes.items():
        if status_codes.get(code):
            sys.stdout.write('{}: {}\n'.format(code, count))
    sys.stdout.flush()
    return None


if __name__ == '__main__':
    main()
