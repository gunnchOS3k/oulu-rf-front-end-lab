import math

def fspl_db(d_km, f_mhz):
    return 32.45 + 20*math.log10(d_km) + 20*math.log10(f_mhz)

def link_budget(tx_dbm, gains, losses):
    return tx_dbm + sum(gains) - sum(losses)
