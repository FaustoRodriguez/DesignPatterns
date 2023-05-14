from patterns import csv_utils
from patterns import web_report,print_report

CSV_FILE = "taxi-data.csv"


def main():
    rides = csv_utils.parse_file(CSV_FILE)
    
    web_report.build_web_report(rides)
    
    print_report.build_print_report(rides)

if __name__ == '__main__':
    main()
