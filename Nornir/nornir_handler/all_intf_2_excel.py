import pandas as pd

def interfaces2excel(nr_results):
    all_intfs = []
    for hostname  ult_result in nr_results.items():
        task_result = mult_result[0]
        interfaces = task_result.result
        if interfaces:
            all_intfs += interfaces
    
    df = pd.DataFrame(all_intfs)
    df.to_excel('interfaces2excel.xlsx'  ndex=False)