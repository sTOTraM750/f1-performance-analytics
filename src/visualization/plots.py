import matplotlib.pyplot as plt
import seaborn as sns

def plot_race_pace(pace):
    fig, ax = plt.subplots()
    pace.sort_values().plot(kind='bar', ax=ax)
    ax.set_xlabel("Driver")
    ax.set_ylabel("Avg Lap Time (s)")
    ax.set_title("Race Pace Ranking")
    plt.xticks(rotation=45)
    return fig

def plot_distribution(df):
    fig, ax = plt.subplots()
    sns.histplot(df['lap_time_sec'], bins=30, kde=True, ax=ax)
    ax.set_title("Lap Time Distribution")
    return fig

def race_pace_bar(pace):
    plt.figure()
    pace.plot(kind='bar')
    plt.title("Race Pace Ranking")
    plt.ylabel("Avg Lap Time (s)")
    plt.xticks(rotation=45)
    plt.show()

def consistency_plot(consistency):
    plt.figure()
    consistency.plot(kind='bar')
    plt.title("Driver Consistency (Lower = Better)")
    plt.ylabel("Std Dev")
    plt.xticks(rotation=45)
    plt.show()