import pfr_package

def test_pfr():
    assert pfr_package.PFR2([10,10],0.05,0.01,0.9) == 'Volume of PFR=90 l'
