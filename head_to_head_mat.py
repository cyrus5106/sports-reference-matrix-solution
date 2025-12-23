import json

def build_head_to_head_tab(data):
    teams = sorted(data.keys())
    header = ["Tm"] + teams
    print("".join(f"{team:>6}" for team in header))
    for row_team in teams:
        row_cells = [f"{row_team:>6}"]
        for col_team in teams:
            if row_team == col_team:
                row_cells.append("  -- ")
            else:
                try:
                    record = data[row_team][col_team]
                    cell = f"{record['W']}-{record['L']}"
                    row_cells.append(f"{cell:>6}")
                except KeyError:
                    row_cells.append("  N/A")
        print(" ".join(row_cells))

