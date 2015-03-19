import numpy

def filter2(window, x):
    range1 = x.shape[0] - window.shape[0] + 1
    range2 = x.shape[1] - window.shape[1] + 1
    x1 = as_strided(x,((x.shape[0] - 10)/1 ,(x.shape[1] - 10)/1 ,11,11), (x.strides[0]*1,x.strides[1]*1,x.strides[0],x.strides[1])) * window
    res = x1.sum((2,3))
    return res


def ssim(img1, img2):
    window = numpy.array([\
        [0.0000,    0.0000, 0.0000, 0.0001, 0.0002, 0.0003, 0.0002, 0.0001, 0.0000, 0.0000, 0.0000],\
        [0.0000,    0.0001, 0.0003, 0.0008, 0.0016, 0.0020, 0.0016, 0.0008, 0.0003, 0.0001, 0.0000],\
        [0.0000,    0.0003, 0.0013, 0.0039, 0.0077, 0.0096, 0.0077, 0.0039, 0.0013, 0.0003, 0.0000],\
        [0.0001,    0.0008, 0.0039, 0.0120, 0.0233, 0.0291, 0.0233, 0.0120, 0.0039, 0.0008, 0.0001],\
        [0.0002,    0.0016, 0.0077, 0.0233, 0.0454, 0.0567, 0.0454, 0.0233, 0.0077, 0.0016, 0.0002],\
        [0.0003,    0.0020, 0.0096, 0.0291, 0.0567, 0.0708, 0.0567, 0.0291, 0.0096, 0.0020, 0.0003],\
        [0.0002,    0.0016, 0.0077, 0.0233, 0.0454, 0.0567, 0.0454, 0.0233, 0.0077, 0.0016, 0.0002],\
        [0.0001,    0.0008, 0.0039, 0.0120, 0.0233, 0.0291, 0.0233, 0.0120, 0.0039, 0.0008, 0.0001],\
        [0.0000,    0.0003, 0.0013, 0.0039, 0.0077, 0.0096, 0.0077, 0.0039, 0.0013, 0.0003, 0.0000],\
        [0.0000,    0.0001, 0.0003, 0.0008, 0.0016, 0.0020, 0.0016, 0.0008, 0.0003, 0.0001, 0.0000],\
        [0.0000,    0.0000, 0.0000, 0.0001, 0.0002, 0.0003, 0.0002, 0.0001, 0.0000, 0.0000, 0.0000]\
    ], dtype=numpy.double)

    K = [0.01, 0.03]
    L = 65535

    C1 = (K[0] * L) ** 2
    C2 = (K[1] * L) ** 2

    mu1 = filter2(window, img1)
    mu2 = filter2(window, img2)

    mu1_sq = numpy.multiply(mu1, mu1)
    mu2_sq = numpy.multiply(mu2, mu2)
    mu1_mu2 = numpy.multiply(mu1, mu2)

    sigma1_sq = filter2(window, numpy.multiply(img1, img1)) - mu1_sq
    sigma2_sq = filter2(window, numpy.multiply(img2, img2)) - mu2_sq
    sigma12 = filter2(window, numpy.multiply(img1, img2)) - mu1_mu2

    ssim_map = numpy.divide(numpy.multiply((2*mu1_mu2 + C1), (2*sigma12 + C2)), numpy.multiply((mu1_sq + mu2_sq + C1),(sigma1_sq + sigma2_sq + C2)))
    return numpy.mean(ssim_map)

def calc_ssim():

    img1 = numpy.array(numpy.zeros((1024,1024)),dtype=numpy.double)
    img2 = numpy.array(numpy.zeros((1024,1024)),dtype=numpy.double)

    return ssim(img1, img2)
