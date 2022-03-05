import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class VisualizeData(object):
    def __init__(self):
        self.df = pd.read_csv('data.csv', sep=',')

    def average_table(self):
        course_completion_rate_avg = self.df.course_completion_rate.mean()
        task_completion_rate_avg = self.df.task_completion_rate.mean()
        feedback_rate_avg = self.df.feedback_rate.mean()
        participation_rate_avg = self.df.participation_rate.mean()

        fig, ax = plt.subplots(1, 1)
        data_to_display = [[course_completion_rate_avg], [task_completion_rate_avg],
                           [feedback_rate_avg], [participation_rate_avg]]

        column_labels = ['Average']

        data_to_display_df = pd.DataFrame(data_to_display, columns=column_labels)
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=data_to_display_df.values,
                         colLabels=data_to_display_df.columns,
                         rowLabels=['Participation', 'Course Completion', 'Task Completion', 'Feedback'],
                         rowColours=['skyblue'] * len(data_to_display_df),
                         colColours=['skyblue'] * len(data_to_display_df.columns),
                         rowLoc='center',
                         loc='center')

        table.scale(1, 2)
        table.set_fontsize(16)

        fig.tight_layout()
        plt.show()

    def scatter_graph(self):
        plt.figure(figsize=(16, 8))
        plt.title('Scatter Graph - Course and Participation')

        sns.scatterplot('course_completion_rate',
                        'participation_rate',
                        hue='id',
                        s=100,
                        data=self.df,
                        size="id",
                        sizes=(25, 250),
                        palette=sns.color_palette('Blues', as_cmap=True),
                        legend='auto')

        plt.figure(figsize=(16, 8))
        plt.title('Scatter Graph - Task and Participation')

        sns.scatterplot('task_completion_rate',
                        'participation_rate',
                        hue='id',
                        s=100,
                        data=self.df,
                        size="id",
                        sizes=(25, 250),
                        palette=sns.color_palette('Blues', as_cmap=True),
                        legend='auto')

        plt.figure(figsize=(16, 8))
        plt.title('Scatter Graph - Feedback and Participation')

        sns.scatterplot('feedback_rate',
                        'participation_rate',
                        hue='id',
                        s=100,
                        data=self.df,
                        size="id",
                        sizes=(25, 250),
                        palette=sns.color_palette('Blues', as_cmap=True),
                        legend='auto')
        plt.grid()
        plt.show()

if __name__ == "__main__":
    v = VisualizeData()
    v.average_table()
    v.scatter_graph()
