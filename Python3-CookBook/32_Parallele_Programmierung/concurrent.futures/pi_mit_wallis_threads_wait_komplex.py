#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent import futures

def naehere_pi_an(n):
    pi_halbe = 1
    zaehler, nenner = 2.0, 1.0
    
    for i in range(n):
        pi_halbe *= zaehler / nenner
        if i % 2:
            zaehler += 2
        else:
            nenner += 2
            
    return 2*pi_halbe


N = (
    12345678,
    123456,
    1234,
    12,
)

with futures.ThreadPoolExecutor(max_workers=4) as e:
    fs = {e.submit(naehere_pi_an, n): n for n in N}
    
    fertig = False
    while not fertig:
        res = futures.wait(fs, timeout=1.0)
        for f in res.done:
            print("n={:10}: {}".format(fs[f], f.result()))
            del fs[f]
        fertig = (len(res.not_done) == 0)

    