#!/usr/bin/env python3

def main(gas_cost_filename: str, latex_output: str):
    with open(gas_cost_filename, "r") as f:
        gas_cost_table = f.readlines()
        gas_cost_table = [line.strip() for line in gas_cost_table]
        for line in gas_cost_table:
            print(line)
    gas_cost_table = gas_cost_table[5:]
    rows = []
    for line in gas_cost_table:
        fields = line.split(" ")
        fields = [field for field in fields if len(field) > 1 or field == "-" or field.isnumeric()]
        if len(fields) > 1:
            rows.append(fields)
    for row in rows:
        print(row)
    with open(latex_output, "w") as f:
        f.write("\\begin{table}[hbtp]\n")
        f.write("\\centering\n")
        f.write("\\begin{tabular}{ |l|r|r|r|r| }\n")
        f.write("\\hline\n")
        f.write(f"\\multicolumn{{1}}{{|>{{\\centering\\arraybackslash}}l|}}{{{rows[0][1]}}} & ")
        f.write(f"\\multicolumn{{1}}{{|>{{\\centering\\arraybackslash}}l|}}{{{rows[0][2]}}} & ")
        f.write(f"\\multicolumn{{1}}{{|>{{\\centering\\arraybackslash}}l|}}{{{rows[0][3]}}} & ")
        f.write(f"\\multicolumn{{1}}{{|>{{\\centering\\arraybackslash}}l|}}{{{rows[0][4]}}} & ")
        f.write(f"\\multicolumn{{1}}{{|>{{\\centering\\arraybackslash}}l|}}{{\\# of calls}} \\\\ \n")
        f.write("\\hline\n")
        for row in rows[1:-2]:
            print(row)
            f.write(f"{row[1]} & {row[2]} & {row[3]} & {row[4]} & {row[5]} \\\\ \n")
            f.write("\\hline\n")
        f.write("\\end{tabular}\n")
        f.write("\\caption{Gas cost evaluation per method}\n")
        f.write("\\label{tab:gas_cost}\n")
        f.write("\\end{table}\n")

if __name__ == "__main__":
    main("gas_cost_output.txt", "latex_output.txt")
