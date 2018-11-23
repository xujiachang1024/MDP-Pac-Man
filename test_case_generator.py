with open("test_cases.txt", "w") as file:
    discount_factors = [1.0, 0.9, 0.8, 0.7, 0.6]
    safety_thresholds = [-200.0, -300.0, -400.0]
    ghostbuster_modes = ["inactive", "defensive", "offensive"]
    for discount_factor in discount_factors:
        for safety_threshold in safety_thresholds:
            for ghostbuster_mode in ghostbuster_modes:
                file.write(str(discount_factor) + ", " + str(safety_threshold) + ", " + str(ghostbuster_mode) + "\n")
