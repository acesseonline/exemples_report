# -*- coding: utf-8 -*-
# GNU GENERAL PUBLIC LICENSE
#
# Copyright (c) 2020 Jadson Bonfim Ribeiro <contato@jadsonbr.com.br>
#
import os
from pyreportjasper import PyReportJasper

RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')


def example_csv():
    input_file = os.path.join(REPORTS_DIR, 'csv.jrxml')
    output_file = os.path.join(REPORTS_DIR, 'csv')
    pyreportjasper = PyReportJasper()
    pyreportjasper.config(
        input_file,
        output_file,
        output_formats=["pdf"],
        db_connection={
            'driver': 'csv',
            'data_file': os.path.join(RESOURCES_DIR, 'csvExampleHeaders.csv'),
            'csv_charset': 'utf-8',
            'csv_out_charset': 'utf-8',
            'csv_field_del': '|',
            'csv_out_field_del': '|',
            'csv_record_del': "\r\n",
            'csv_first_row': True,
            'csv_columns': "Name,Street,City,Phone".split(",")
        }
    )
    pyreportjasper.process_report()
    output_file = output_file + '.pdf'
    if os.path.isfile(output_file):
        print('Report generated successfully!')


if __name__ == '__main__':
    example_csv()
