import base64
from io import BytesIO

import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


def image_from_base64(image_base64: str) -> Image:
    """The function returns an image from a base64 string.
    """
    return Image.open(BytesIO(base64.b64decode(image_base64)))


def determine_colors(image: Image) -> tuple:
    """Determines main colors of the image using KMeans.
    """
    # prepare image for KMeans
    bands = image.split()

    rgb = [np.asarray(band).flatten() for band in bands[:4]]
    reshape = np.array(
        [[rgb[0][i], rgb[1][i], rgb[2][i]] for i in range(rgb[0].shape[0])]
    )
    cluster = KMeans(n_clusters=5).fit(reshape)

    # get clusters to determine the primary colors
    centroids = cluster.cluster_centers_
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (hist, _) = np.histogram(cluster.labels_, bins=labels)
    hist = hist.astype('float')
    hist /= hist.sum()

    colors = sorted(
        [(percent, color) for (percent, color) in zip(hist, centroids)],
        reverse=True,
        key=lambda x: x[0]
    )

    return colors


def rgb2hex(r, g, b):
    if (r + g + b) / 3 > 220:
        text_color = '#212529'
    else:
        text_color = '#fff'
    return {
        'text': text_color,
        'bg': '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))
    }
