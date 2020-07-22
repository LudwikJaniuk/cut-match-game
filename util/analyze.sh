# run.py outputs with periods, but google sheets will only take commas.
python3 run.py a | sed "s/\./,/g"
