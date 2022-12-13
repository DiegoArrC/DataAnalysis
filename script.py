import pandas as pd 
import numpy as npy
import matplotlib.pyplot as plots

def create_plot_1(main_df):

    body_by_equipment = main_df.groupby(["equipment","bodyPart"])["equipment"].count().unstack().fillna(0)
    # creates a plot based on each exercise equipment
    fig, ax = plots.subplots()

    bottom = npy.zeros(len(body_by_equipment))
    # iterates through each columns and stacks each bar of the dataframe
    for i, col in enumerate(body_by_equipment.columns):
        ax.bar(body_by_equipment.index, body_by_equipment[col], bottom=bottom,label=col)
        bottom+= npy.array(body_by_equipment[col])
    
    label_plot(ax,body_by_equipment)

def label_plot(ax,df):
    # establishes the sums for each bar
    totals = df.sum(axis=1)
    # adds labels of each total to each bar
    for i,total in enumerate(totals):
        ax.text(totals.index[i], total + 4, round(total), ha='center', weight = 'bold')
    #adds labels to each subtotal within each bar
    for bar in ax.patches:
        if bar.get_height() >= 10:     
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + bar.get_y() + -10,
                round(bar.get_height()),
                ha='center',
                color='w',
                weight='bold',
                size=8)
    ax.set_xlabel("Equipment")
    ax.set_ylabel("Quantity of Body Parts")
    ax.set_title('Body Part Distribution by Equipment')
    ax.legend()
    plots.xticks(rotation=90)
    

# # each body area and target muscle with different equipment values
def create_plot_2(main_df):

    equipment_by_target = main_df.groupby(["bodyPart","target","equipment"])["equipment"].count().unstack().fillna(0)

    print(equipment_by_target) #before setting multi-index
    print(len(equipment_by_target))
    print("-" * 20)
    ax = equipment_by_target.plot.bar(stacked=True) #currently works
    # label_plot(ax,equipment_by_target)


    bottom = npy.zeros(len(equipment_by_target))


def showplots():
    plots.show()
def main():
    fitness_exercises = pd.read_csv("fitness_exercises.csv")
    create_plot_1(fitness_exercises)
    showplots()
    create_plot_2(fitness_exercises)
    showplots()

if __name__ == "__main__":
    main()