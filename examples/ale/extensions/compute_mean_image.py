import numpy as np
from utils import data, viewer


def compute_mean_image(frames):
    frame = frames[0]
    print('shape: {}'.format(frame.shape))
    assert frame.shape == (210, 160, 3)

    mean_image = np.zeros(shape=(210, 160, 3), dtype=np.float32)
    N = len(frames)
    for frame in frames:
        mean_image += frame / 255
    return mean_image / N


def assert_is_in_range(value, min=0.0, max=1.0):
    assert not (value < 0 or 1 < value)

def main():
    states = data.load_data('../states/10000.pickle')
    frames = [state['frame'] for state in states]
    mean_image = compute_mean_image(frames)

    viewer.show_image(mean_image)
    max_rgb = np.max(mean_image)
    max_r = np.max(mean_image[:, :, 0])
    max_g = np.max(mean_image[:, :, 1])
    max_b = np.max(mean_image[:, :, 2])
    min_r = np.min(mean_image[:, :, 0])
    min_g = np.min(mean_image[:, :, 1])
    min_b = np.min(mean_image[:, :, 2])
    med_r = np.median(mean_image[:, :, 0])
    med_g = np.median(mean_image[:, :, 1])
    med_b = np.median(mean_image[:, :, 2])

    print('max_rgb: {}'.format(max_rgb))
    print('max_r: {}, max_g: {}, max_b: {}'.format(max_r, max_g, max_b))
    print('med_r: {}, med_g: {}, med_b: {}'.format(med_r, med_g, med_b))
    print('min_r: {}, min_g: {}, min_b: {}'.format(min_r, min_g, min_b))

    assert_is_in_range(max_r)
    assert_is_in_range(max_g)
    assert_is_in_range(max_b)

    assert_is_in_range(min_r)
    assert_is_in_range(min_g)
    assert_is_in_range(min_b)

if __name__ == '__main__':
    main()
