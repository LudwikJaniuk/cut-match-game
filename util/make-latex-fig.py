#!python3
import sys
import math

# Used to generate latex code for myself. Don't know if useful

lines = iter(sys.stdin)
next(lines)
lines = map(lambda s: s.replace("_", "\\_").split(), lines)

#0 Graph_name	vertices	edges	g_phi	h_phi	timed_out	
#6 spent_time	allowed_time	read_as_multi	CASE	best_cut_conductance	
#11 best_cut_expansion	edges_crossing	size1	size2	diff_total	
#16 diff_div_nodes	vol1	vol2	best_round	last_round
#21 walsh_cond	walsh_imb colr  colg    colb    h_s_expan h_s_expan_l
#28 walsh_cross
print(f"{4}")

def condform(n):
    if float(n) == 0:
        return ret
    if n[0] == '0':
        return n[1:]
    return n

def main_table():
    for line in lines:
        # This should NOT be percent
        for i in [16, 22]:
            line[i] = "{:.3%}".format(float(line[i])).replace("%","")
        #for i in [26, 27]:
       #     line[i] = "{:.3f}".format(float(line[i]))


        latex = (
                f"\\textbf{{{line[0]}}} & \\multirow{{2}}*{{{line[19]} / {line[20]}}} &  {line[10]}   & {line[16]} & {line[12]} & {line[26]}   \\\\\n" 
                f" \multicolumn{{1}}{{|r|}}{{{line[7]}}} & &  {line[21]} & {line[22]} & {line[28]} & {line[27]}   \\\\ \n"
                f"\\hline"

        )
        print(latex)

def g_table():
    for line in lines:
        v = int(line[1])
        cond = line[10]
        oversqrt = condform("{:.6f}".format(1.0/math.sqrt(v)))
        overlog2 = condform("{:.6f}".format(1.0/math.log(v)))
        overloglog = condform("{:.6f}".format(1.0/math.log(math.log(v))))
        latex = (
                f"\\textbf{{{line[0]}}} & {cond} & {oversqrt} & {overlog2} & {overloglog} \\\\ \n"
                f"%\\hline"
        )
        print(latex)

if len(sys.argv) == 2:
    assert(sys.argv[1] == "g")
    g_table()
else:
    main_table()

