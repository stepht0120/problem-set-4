'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def plot_fta_bar(pre_universe):
    '''
    creates a bar plot for the 'fta' column.
    
    args:
        pre_universe (pd.DataFrame): dataFrame containing the data.
    '''
    sns.countplot(data=pre_universe, x='fta')
    plt.title('FTA Bar Plot')
    plt.savefig('./data/part3_plots/fta_barplot.png', bbox_inches='tight')
    plt.close()


# 2. Hue the previous barplot by sex
def plot_fta_bar_hue_by_sex(pre_universe):
    '''
    creates a bar plot for the 'fta' column, hued by 'sex'.
    
    Args:
        pre_universe (pd.DataFrame): dataFrame containing the data.
    '''
    sns.countplot(data=pre_universe, x='fta', hue='sex')
    plt.title('FTA Bar Plot Hued by Sex')
    plt.savefig('./data/part3_plots/fta_barplot_hue_sex.png', bbox_inches='tight')
    plt.close()


# 3. Plot a histogram of age_at_arrest
def plot_age_histogram(pre_universe):
    '''
    Creates a histogram for the 'age_at_arrest' column.
    
    Args:
        pre_universe (pd.DataFrame): DataFrame containing the data.
    '''
    sns.histplot(data=pre_universe, x='age_at_arrest')
    plt.title('Histogram of Age at Arrest')
    plt.savefig('./data/part3_plots/age_histogram.png', bbox_inches='tight')
    plt.close()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def plot_age_histogram_binned(pre_universe):
    '''
    Creates a histogram for the 'age_at_arrest' column with specific bins representing age groups.
    
    Args:
        pre_universe (pd.DataFrame): DataFrame containing the data.
    '''
    bins = [18, 21, 30, 40, 100]
    sns.histplot(data=pre_universe, x='age_at_arrest', bins=bins)
    plt.title('Histogram of Age at Arrest with Specific Bins')
    plt.savefig('./data/part3_plots/age_histogram_binned.png', bbox_inches='tight')
    plt.close()


