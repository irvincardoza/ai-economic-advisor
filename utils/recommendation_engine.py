def generate_recommendations(economic_condition):
    if economic_condition == "inflation":
        return ["Invest in inflation-protected securities (TIPS)", "Diversify into defensive sectors"]
    elif economic_condition == "recession":
        return ["Shift to bonds", "Cut cyclical stock exposure"]
    else:
        return ["Maintain balanced portfolio", "Dollar-cost averaging"]
