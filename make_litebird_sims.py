import numpy as np
import healpy as hp
import pysm
import os
from pysm.litebird_models import models
from pysm.litebird_observation import *


Nsims = 1
out_dir = '/Users/niki/Workspace/LiteBIRD/sky_sims/sims_may14/'
for i in range(Nsims):
    cmb_in = make_cmb(out_dir=out_dir, prefix='cmb_input_'+str(i))
    cmb_file = out_dir+'cmb_input_'+str(i)+'.fits'
    sky_cmb = make_sky_cmb(
        cmb_model='LBc0', cmb_in=cmb_file)
    sky_fg = make_sky_fg(
        nside=512, dust_model='LBd0', synch_model='LBs0')
    sky_tot = make_sky_tot(
        nside=512, dust_model='LBd0', synch_model='LBs0', cmb_model='LBc0', cmb_in=cmb_file)
    litebird_inst_cmb = make_litebird_instrument_noisless(
        out_dir=out_dir, prefix='cmb_observed_'+str(i))
    litebird_inst_fg = make_litebird_instrument_noisless(
        out_dir=out_dir, prefix='fg_observed_'+str(i))
    litebird_inst = make_litebird_instrument(
        seed=None, out_dir=out_dir, prefix='sig_observed_'+str(i))
    obs_cmb = observe_sky(sky_cmb, litebird_inst_cmb)
    obs_fg = observe_sky(sky_fg, litebird_inst_fg)
    obs_tot = observe_sky(sky_tot, litebird_inst)
