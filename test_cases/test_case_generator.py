with open("test_cases.txt", "w") as file:
    file.write("discount_factor, safety_distance, ghostbuster_mode\n")
    discount_factors = [1.0, 0.9, 0.8, 0.7, 0.6]
    safety_distances = [4, 3, 2, 1]
    ghostbuster_modes = ["inactive", "defensive", "offensive"]
    file.write("-----------------\n")
    for discount_factor in discount_factors:
        for safety_distance in safety_distances:
            for ghostbuster_mode in ghostbuster_modes:
                file.write(str(discount_factor) + ", " + str(safety_distance) + ", " + str(ghostbuster_mode) + "\n")
        file.write("-----------------\n")
