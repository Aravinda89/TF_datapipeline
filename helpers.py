import matplotlib.pyplot as plt
from numpy.random import randint

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