Example package
===============

This package has function to design a Plug Flow Reactor. 
We do this for a specific conversion, assuming that we know the requirement of production (which is generally the case in industries).

Assumptions:

1. Synthesis reaction (${A+B→C}$)
2. Gas-phase reaction
3. Ideal Gas Law
4. Elementary Rate Laws
5. Stoichiometric coefficients of A and B are set to 1



Function Inputs (SI units):
1. Inlet Molar Flows of A and B (mol/s)
2. Inlet Volumetric flowrate (m^3/s)
3. Rate constant (m^3/(mol-s))
4. Conversion (wrt A)

Function Outputs:
1. Reactor Volume
2. Outlet Molar Flows of A,B,C.
