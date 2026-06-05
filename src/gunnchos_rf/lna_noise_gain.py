def nf_to_noise_temp(nf_db, t0=290):
    return t0*(10**(nf_db/10)-1)
