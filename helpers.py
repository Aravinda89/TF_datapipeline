import matplotlib.pyplot as plt
from numpy.random import randint
import pygal 
import os
from IPython.display import display, HTML

def display_imgs(imgs, labels, class_names, fig_size=(10,10)):
    """
    Display Random Images

    train_imgs: image list numpy array
    train_labels: labels numpy array
    class_names: list
    fig_size: (width, height)
    """
    random_index = randint(0, len(imgs), 1)[0]
    plt.figure(figsize=fig_size)
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(True)
        plt.imshow(imgs[random_index+i], cmap=plt.cm.binary)
        plt.xlabel(class_names[labels[random_index+i][0]])
    plt.show()
    

def class_count(class_names, labels_list, name='Distribution'):
    """
    Display class count
    
    class_names: list in order
    labels_list: list
    """
    
    #Create function to display interactive plotting
    base_html = """
    <!DOCTYPE html>
    <html>
      <head>
      <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/svg.jquery.js"></script>
      <script type="text/javascript" src="https://kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js""></script>
      </head>
      <body>
        <figure>
          {rendered_chart}
        </figure>
      </body>
    </html>
    """

    def galplot(chart):
        rendered_chart = chart.render(is_unicode=True)
        plot_html = base_html.format(rendered_chart=rendered_chart)
        display(HTML(plot_html))

    #Compare class distribution
    line_chart = pygal.Bar(height=300)
    line_chart.title = name

    for idx,i in enumerate(class_names):
        line_chart.add(i, labels_list.count(idx))
    galplot(line_chart)