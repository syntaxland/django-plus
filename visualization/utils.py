import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64


# def get_graph():
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     # image_png = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
#     image_png = buffer.getvalue()
#     graph = base64.b64encode(image_png)
#     graph = graph.decode('utf-8')
#     buffer.close()
#     return graph

# def get_plot(x,y):
#     plt.switch_backend('AGG')
#     plt.figure(figsize=(10,8))
#     plt.title('Sales')
#     plt.plot(x,y)
#     plt.xticks(rotation=45)
#     plt.xlabel('Item')
#     plt.ylabel('Price')
#     plt.tight_layout()
#     graph = get_graph()
#     return graph


# Adding seaborn
def get_plot(x, y):
    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(7,5))
    ax.set_title('Sales')

    # sns.barplot(x=x, y=y, color='blue', ax=ax)
    # sns.scatterplot(x=x, y=y, ax=ax)
    sns.lineplot(x=x, y=y, ax=ax)
    # sns.countplot(x=x, y=y, color='blue', ax=ax)
    # sns.boxplot(x=x, y=y, color='blue', ax=ax)
    # sns.violinplot(x=x, y=y, color='blue', ax=ax)
    # sns.swarmplot(x=x, y=y, color='blue', ax=ax)
    # sns.heatmap(x=x, y=y, color='blue', ax=ax)
    # sns.pairplot(x=x, y=y, color='blue', ax=ax)

    ax.set_xticklabels(labels=x, rotation=45, ha='right')
    ax.set_xlabel('Item')
    ax.set_ylabel('Price')
    plt.tight_layout()

    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()

    return graph



