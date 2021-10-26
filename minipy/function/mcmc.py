def metropolis_hasting_sampling(p, T=10000, combustion_period=100, thetamin=-10, thetamax=10, q_sigma=1):
    assert T > combustion_period
    import random
    from scipy.stats import norm
    '''
    :param
        p: give the target distribution $P$.
        T: sampling epochs
        combution_period: samples before combution_period are all discarded
        thetamin: lower bound of the initial range
        thetamax: upper bound of the initial range
        q_sigma: variance of proposal distribution q
    :return
        list of samples from target distribution p
    '''

    theta = [0.0] * (T+1)
    theta[0] = random.uniform(thetamin, thetamax)

    for t in range(T):
        # 从均值为theta[t]，方差为q_sigma的正态分布q中生成候选状态
        # q(x1, x2)此处表示均值为x1，样本取到x2的概率
        theta_star = norm.rvs(loc=theta[t], scale=q_sigma, size=1, random_state=None)
        alpha = min(1, (p(theta_star[0]) / p(theta[t])))
        u = random.uniform(0, 1)
        if u <= alpha:
            theta[t + 1] = theta_star[0]  # 接收状态跳转
        else:
            theta[t + 1] = theta[t]  # 拒绝状态跳转

    return theta[combustion_period::]


def gibbs_sampling(p, dim, combustion_period=100, T=2021, thetamin=-10, thetamax=10, q_sigma=1):
    assert T > combustion_period
    import random
    from scipy.stats import norm
    '''
    :param
        p: give the target distribution $P$.
        T: sampling epochs
        combution_period: samples before combution_period are all discarded
        thetamin: lower bound of the initial range
        thetamax: upper bound of the initial range
        q_sigma: variance of proposal distribution q
    :return
        list of samples from target distribution p
    '''

    x_res = [(random.uniform(thetamin, thetamax), random.uniform(thetamin, thetamax))]

    for i in range(T):
        for j in range(dim):
            x_now = x_res[-1]
            xj_now = x_now[j]
            xj_new = norm.rvs(loc=xj_now, scale=q_sigma, size=1, random_state=None)[0]
            x_new = [xj_new if a==j else x_now[a] for a in range(dim)]
            alpha = min(1, (p(x_new) / p(x_now)))
            u = random.uniform(0, 1)
            if u <= alpha:
                x_res.append(x_new) # 接收状态跳转
            else:
                x_res.append(x_now) # 拒绝状态跳转

    return x_res[combustion_period::]