""" Testing functions used to process data in data_process.py

data_process.py uses the pandas library. Functions used are chained
 e.g. groupby and nunique
 
 The chained commands are tested.
"""

import pandas as pd
import pytest

def test_mult_groupby_uniq_counts():
    """Test grouping by multiple columns with unique counts"""

    # Example data frame
    df = pd.DataFrame({'mutated_from_allele': ['A',    'A',    'A',    'A',     'A', 'G'],
                       'mutated_to_allele'  : ['T',    'T',    'T',    'C',     'C' ,'C'],
                       'icgc_mutation_id'   : ['ID_1', 'ID_2', 'ID_1', 'ID_3', 'ID_4', 'ID_5']
                      })
                      
    # The expected result is for each unique combination of 
    #   mutation_from_allele, mutation_to_allele
    #   report the unique number of icgc_mutation_id
    #			   
    expected_dfg = pd.DataFrame({'mutated_from_allele': ['A', 'A', 'G'],
                                 'mutated_to_allele'  : ['C', 'T', 'C'],
                                 'icgc_mutation_id'   : [ 2 ,  2,   1]
                                })
    dfg = df.groupby(['mutated_from_allele','mutated_to_allele'], as_index=False)['icgc_mutation_id'].nunique()	   
    
    assert dfg.equals(expected_dfg) == True
       
def test_min():
    """Test finding group with minimum unique count"""
    df = pd.DataFrame({'icgc_sample_id'   : ['S1', 'S2', 'S1', 'S2', 'S3', 'S1'],
                       'icgc_mutation_id': ['M1', 'M1', 'M1', 'M2', 'M2', 'M3']})
                       
    min_idx = (df.groupby('icgc_sample_id')['icgc_mutation_id']
                 .nunique()
                 .idxmin()
            )

    min_value = (df.groupby('icgc_sample_id')['icgc_mutation_id']
                    .nunique()
                   .loc[min_idx]
                )
    assert min_idx == 'S3' and min_value == 1
    
    
def test_max():
    """Test finding group with maximum unique count"""
    df = pd.DataFrame({'icgc_sample_id'   : ['S1', 'S2', 'S1', 'S2', 'S3', 'S1'],
                       'icgc_mutation_id': ['M1', 'M1', 'M1', 'M2', 'M2', 'M3']})

    max_idx = (df.groupby('icgc_sample_id')['icgc_mutation_id']
                 .nunique()
                 .idxmax()
            )

    max_value = (df.groupby('icgc_sample_id')['icgc_mutation_id']
                   .nunique()
                  .loc[max_idx]
                )
    assert max_idx == 'S1' and max_value == 2

if __name__ == '__main__':
    print("Test debugging - running tests outside of pytest")
    test_mult_groupby_uniq_counts()
    test_min()
    test_max()