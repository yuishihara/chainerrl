from . import data
import matplotlib.pyplot as plt
import matplotlib.animation as pltanim


def create_window(image, is_gray=False):
    if is_gray:
        return plt.imshow(image, cmap='gray')
    else:
        return plt.imshow(image)


def show_image(image, is_gray=False):
    create_window(image, is_gray=is_gray)
    plt.show()


def animate(images, is_gray=False, save_gif=False):
    fig = plt.figure()
    im = create_window(images[0], is_gray=is_gray)

    def init():
        im.set_data(images[0])

    def update(index):
        im.set_data(images[index])
        return im

    anim = pltanim.FuncAnimation(fig, update, init_func=init, frames=len(images), interval=10)
    if save_gif:
        anim.save('anim.gif', writer='imagemagick')
    plt.show()
