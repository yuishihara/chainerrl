import data as dutils
import viewer


def show_frame(frame):
    viewer.show_image(frame, is_gray=False)


def animate_frames(frames):
    viewer.animate(frames, is_gray=False)


def main():
    filename = '../../states/20000states.pickle'
    states = dutils.load_data(filename)
    state = states[0]
    # frame = state['frame']
    # show_frame(frame)

    frames = [state['frame'] for state in states]
    animate_frames(frames)


if __name__ == '__main__':
    main()
