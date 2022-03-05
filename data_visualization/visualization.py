import matplotlib.pyplot as plt
import pandas as pd


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


if __name__ == "__main__":
    v = VisualizeData()
    v.average_table()
