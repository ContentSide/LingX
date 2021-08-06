import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def plot_complexity_profiling(input, tokens_scores_list, type_x="IDT"):
    x_values = []
    y_values = []
    for token, score in tokens_scores_list:
        x_values.append(token)
        y_values.append(score)


    figure(figsize=(20, 5), dpi=80)

    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off


    for i, txt in enumerate(x_values):
        plt.annotate(txt, (i, y_values[i]))

    plt.xlabel('Tokens')
    plt.ylabel('Complexity Score')
    plt.title(type_x + " Complexity profiling for sentece :"+ input)

    plt.plot(range(len(x_values)),y_values)
    plt.show()