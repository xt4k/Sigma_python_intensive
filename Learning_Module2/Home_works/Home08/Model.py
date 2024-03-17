def Model(n):
    '''

    :param n:
    :return:
    '''

    import numpy as np
    S0 = np.zeros((n))
    for i in range(n):
        S0[i] = (0.0000005 * i * i)  # real process square model
    return S0
