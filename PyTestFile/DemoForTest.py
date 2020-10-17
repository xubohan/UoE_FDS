from datascience import *
import numpy as np
data = 'http://www2.census.gov/programs-surveys/popest/datasets/2010-2015/national/asrh/nc-est2015-agesex-res.csv'

if __name__ == '__main__':
    tableData = Table.read_table(data)
    sappDtata = tableData.select('SEX', 'AGE', 'POPESTIMATE2010', 'POPESTIMATE2014')
    sappDtata = sappDtata.relabel('POPESTIMATE2010', '2010' ).relabel('POPESTIMATE2014', '2014')
