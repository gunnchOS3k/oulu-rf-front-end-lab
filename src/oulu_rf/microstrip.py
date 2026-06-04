def effective_er(er, h, w):
    return (er+1)/2 + (er-1)/2 * (1+12*h/w)**-0.5
