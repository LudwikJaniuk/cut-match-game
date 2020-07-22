# Run with a memory limit, not to go into paging shoudl the process get too hungry
ulimit -Sv 10240000000
python3 run.py r
