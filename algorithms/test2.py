import math

def calculate_max_quality_score(impact_factor, ratings):
    n = len(ratings)
    
    # Step 1: Calculate the original max quality score using Kadane's algorithm
    def kadane(arr):
        max_so_far = float('-inf')
        max_ending_here = 0
        for val in arr:
            max_ending_here += val
            max_so_far = max(max_so_far, max_ending_here)
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

    original_max_score = kadane(ratings)

    # Step 2: Amplify Strategy
    # Compute maximum sum when amplifying a single subarray
    max_amplified_score = float('-inf')
    amplified = [rating * impact_factor for rating in ratings]
    for i in range(n):
        max_amplified_score = max(max_amplified_score, amplified[i])

    # Subarray Delta Amplify (Sliding Window with Kadane)
    max_amplified_score = kadane(amplified)

    # Step 3: Adjust Strategy
    # Compute maximum sum when adjusting a single subarray
    adjusted_ratings = [
        math.ceil(value / impact_factor) for value in ratings] # ]
        if      value =]
        :
            ...
    

        










