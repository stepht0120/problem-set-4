'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?

def felony_nonfelony_scatter(merged_df):
    """
    creates a scatter plot with lmplot where the x-axis is the prediction for felony,
    the y-axis is the prediction for non-felony, and the hue is whether the current charge is a felony.

    Args:
        merged_df (pd.DataFrame): the merged dataframe containing arrest data and prediction data.
    """
    sns.lmplot(data = merged_df, x = 'prediction_felony', y = 'prediction_nonfelony', hue = 'has_felony_charge', fit_reg = False)
    plt.title('Felony vs. Non-Felony Predictions, Hued by Current Felony Charge')
    plt.savefig('./data/part5_plots/felony_nonfelony_scatter.png', bbox_inches = 'tight')
    plt.close()

    print("the group of dots on the right side of the plot represent individuals with a high probability of felony rearrest.")


# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?

def felony_prediction_vs_actual_scatter(merged_df):
    """
    creates a scatter plot where the x-axis is the prediction for felony rearrest,
    and the y-axis is whether someone was actually rearrested.

    Args:
        merged_df (pd.DataFrame): the merged dataframe containing arrest data and prediction data.
    """
    sns.lmplot(data = merged_df, x = 'prediction_felony', y = 'rearrested_felony', fit_reg = False)
    plt.title('Felony Prediction vs. Actual Rearrest')
    plt.savefig('./data/part5_plots/felony_prediction_vs_actual_scatter.png', bbox_inches='tight')
    plt.close()

    print("based on the plot, the model may not be well calibrated because the points do not seem to align with the expected outcomes.")

