#!/usr/bin/env python3

""" Script to process ICGC simple somatic data file

Process file from ICGC (International Cancer Genome Consortium):
https://dcc.icgc.org/releases/current/Projects/BLCA-CN/
 simple_somatic_mutation.open.BLCA-CN.tsv.gz

Release_28 Dowloaded on 2022-09-08

Reports 
- patterns of mutated allele and number of uniq icgc_mutation_ids
- icgc_sample_id with highest and lowest unique icgc_mutation_id count
"""

import pandas as pd;

def mutation_patterns(df):
    """Report mutation patterns and number of unique icgc_mutation_id"""
    ds_allele_count = df.groupby(['mutated_from_allele','mutated_to_allele'], as_index=False)['icgc_mutation_id'].nunique()
    ds_allele_count = ds_allele_count.rename(columns = {'icgc_mutation_id':"Count of unique_mutation_id"})
    print("\nCounts of unique icgc_mutation_id by mutation patterns\n")
    print(ds_allele_count.to_string(index=False))

def sample_report(df):
    """Report igc_sample_id with min and max unique igc_mutation_id count"""
    ds_sample_max = (df.groupby('icgc_sample_id')['icgc_mutation_id']
                       .nunique()
                       .idxmax()
                    )
    max_count = (df.groupby('icgc_sample_id')['icgc_mutation_id']
               .nunique()
               .loc[ds_sample_max]
            )
    print(f'\nicgc_sample_id {ds_sample_max} has highest unique icgc_mutation_id count of {max_count}')

    ds_sample_min = (df.groupby('icgc_sample_id')['icgc_mutation_id']
                        .nunique()
                        .idxmin()
                    )

    min_count = (df.groupby('icgc_sample_id')['icgc_mutation_id']
                   .nunique()
                   .loc[ds_sample_min]
                )
    print(f'\nicgc_sample_id {ds_sample_min} has lowest unique icgc_mutation_id count of {min_count}')

def main():
    file = 'simple_somatic_mutation.open.BLCA-CN.tsv.gz'
    df = pd.read_csv(file, sep="\t")
    print(f'File: {file}')
  
    mutation_patterns(df)
    sample_report(df)

if __name__ == '__main__':
    main()
