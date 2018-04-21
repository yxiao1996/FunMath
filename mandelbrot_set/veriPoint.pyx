def veriPoint(re, im, thresh=100):
    x = complex(0, 0)
    c = complex(re, im)
    for i in range(thresh):
        x = x * x + c
        if abs(x.real) > 2.0 or abs(x.imag) > 2.0:
            return False
    return True

def veriPoint_c(float re, float im):
    cdef int thresh = 30
    cdef float old_re = 0
    cdef float old_im = 0
    cdef float new_re
    cdef float new_im
    for i in range(thresh):
        new_re = old_re * old_re - old_im * old_im + old_re
        new_im = 2 * old_re * old_im + old_im
        old_re = new_re
        old_im = new_im
    if abs(new_im) > 2.0 or abs(new_re) > 2.0:
        return False
    else:
        return True