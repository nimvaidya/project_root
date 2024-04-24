#!/usr/bin/env python
import numpy as np
from scipy.integrate import solve_ivp

def PFR(F0,v0,k,XA):
    FA0,FB0=F0
    FA_in=FA0*(1-XA)
    FT0=FA0+FB0
    
    def dFdV(V,F):
        FA,FB,FC=F
        FT=FA+FB+FC
        v=v0*FT/FT0
        CA=FA/v
        CB=FB/v
        CC=FC/v
        r=k*CA*CB
        dFAdV=-r
        dFBdV=-r
        dFCdV=r
        return [dFAdV,dFBdV,dFCdV]
    
    def event(V,F):
        FA,FB,FC=F
        return FA_in-FA
    
    event.isterminal=True
    event.direction=0
    
    bigV=10000 #m^3
    V_eval=np.linspace(0,bigV)
    sol=solve_ivp(dFdV,[0,bigV],[FA0,FB0,0],t_eval=V_eval,events=event)
    FA_exit=sol.y_events[0][0][0]
    FB_exit=sol.y_events[0][0][1]
    FC_exit=sol.y_events[0][0][2]
    V=sol.t_events[0][0]
    
    return [V,FA_exit,FB_exit,FC_exit]
