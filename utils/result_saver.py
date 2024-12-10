import pandas as pd
import csv

def save_results(test_results):
    # Save to CSV
    with open("test_results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Page URL", "Test Case", "Result", "Comments"])
        writer.writerows(test_results) 
    
    # Group the test results by test case (assuming 'Test Case' column contains test names)
    grouped_results = {}
    for result in test_results:
        test_case = result[1] 
        if test_case not in grouped_results:
            grouped_results[test_case] = []
        grouped_results[test_case].append(result)
    
    # Save to Excel with multiple sheets for each test case
    with pd.ExcelWriter('test_results.xlsx') as writer:
        for test_case, results in grouped_results.items():
            # Convert the results to a DataFrame for each test case
            df = pd.DataFrame(results, columns=["Page URL", "Test Case", "Result", "Comments"])
            
            df.to_excel(writer, sheet_name=test_case, index=False)


