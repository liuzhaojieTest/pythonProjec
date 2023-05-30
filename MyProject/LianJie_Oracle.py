class LinaJieOracle(object):
    import cx_Oracle

    NDMC1 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC1_BETA')
    NDMC2 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC2_BETA')
    NDMC3 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC3_BETA')
    NDMC4 = cx_Oracle.connect('NDMC', '123456', '122.112.235.69:8521/NDMC4_BETA')