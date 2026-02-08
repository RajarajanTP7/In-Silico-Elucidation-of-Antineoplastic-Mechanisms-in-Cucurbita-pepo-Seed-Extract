$SCHRODINGER/desmond/md_run \
  -JOBNAME HER2_Linoleic_MD \
  -in system_out.cms \
  -time 100 \
  -ensemble NPT \
  -temp 300 \
  -pressure 1.01325 \
  -traj_interval 100 \
  -energy_interval 1.2 \
  -cfg md.msj
