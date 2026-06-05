def mixer_nf_cascade(nf1, nf2, gain1):
    return nf1 + (nf2-1)/gain1
