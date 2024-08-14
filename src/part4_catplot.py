'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.


# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# 
# In a print statement, answer the following question: What might explain the difference between the plots?


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def extract_transform():
    """
    extracts and transforms data from arrest records for analysis.

    Returns:
        - `pred_universe`: the dataframe containing prediction-related data for individuals
        - `arrest_events`: the dataframe containing arrest event data
        - `charge_counts`: a dataframe with counts of charges aggregated by charge degree
        - `charge_counts_by_offense`: a dataframe with counts of charges aggregated by both charge degree and offense category
        - `felony_charge`: a dataframe indicating whether an arrest has at least one felony charge
        - `merged_df`: a merged dataframe containing `pre_universe` and `felony_charge`
    """
    # load data
    pred_universe = pd.read_csv('your_path_to_pre_universe.csv')
    arrest_events = pd.read_csv('your_path_to_arrest_events.csv')

    # create felony_charge dataframe
    felony_charge = arrest_events.groupby('arrest_id').apply(
        lambda x: pd.Series({
            'has_felony_charge': any(x['charge_degree'] == 'FELONY')
        })
    ).reset_index()

    # merge felony_charge with pred_universe
    merged_df = pd.merge(pred_universe, felony_charge, on = 'arrest_id', how = 'left')

    # create additional dataframes
    charge_counts = arrest_events.groupby(['charge_degree']).size().reset_index(name='count')
    charge_counts_by_offense = arrest_events.groupby(['charge_degree', 'offense_category']).size().reset_index(name = 'count')
    
    return pred_universe, arrest_events, charge_counts, charge_counts_by_offense, felony_charge, merged_df

def plot_felony_rearrest_predictions(merged_df):
    """
    creates a catplot for charge type with the y-axis as prediction for felony rearrest.

    Args:
        merged_df (pd.DataFrame): the merged dataframe containing arrest data and prediction data.
    """
    sns.catplot(data = merged_df, x = 'charge_degree', y = 'prediction_felony', kind = 'bar')
    plt.title('Prediction for Felony Rearrest by Charge Type')
    plt.savefig('./data/part4_plots/felony_rearrest_predictions.png', bbox_inches='tight')
    plt.close()

def plot_nonfelony_rearrest_predictions(merged_df):
    """
    creates a catplot for charge type with the y-axis as prediction for non-felony rearrest.

    Args:
        merged_df (pd.DataFrame): the merged dataframe containing arrest data and prediction data.
    """
    sns.catplot(data = merged_df, x = 'charge_degree', y = 'prediction_nonfelony', kind = 'bar')
    plt.title('Prediction for Non-Felony Rearrest by Charge Type')
    plt.savefig('./data/part4_plots/nonfelony_rearrest_predictions.png', bbox_inches='tight')
    plt.close()

def plot_felony_rearrest_predictions_hue_actual(merged_df):
    """
    creates a catplot for charge type with the y-axis as prediction for felony rearrest,
    hued by whether the person actually got rearrested for a felony crime.

    Args:
        merged_df (pd.DataFrame): the merged dataframe containing arrest data and prediction data.
    """
    sns.catplot(data = merged_df, x = 'charge_degree', y = 'prediction_felony', hue = 'rearrested_felony', kind = 'bar')
    plt.title('Prediction for Felony Rearrest by Charge Type, Hued by Actual Rearrest')
    plt.savefig('./data/part4_plots/felony_rearrest_predictions_hue_actual.png', bbox_inches = 'tight')
    plt.close()

def main():
    # load and transform data
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense, felony_charge, merged_df = extract_transform()

    # generate the plots
    plot_felony_rearrest_predictions(merged_df)
    plot_nonfelony_rearrest_predictions(merged_df)
    plot_felony_rearrest_predictions_hue_actual(merged_df)

    # print explanations
    print("")
