import numpy
import cPickle
import gzip
import os
from utils import *
# 在终端输入conda config --add channels conda-forge


class RBM(object):
    def __init__(self, input=None, n_visible=28*28, n_hidden=500,
                 W=None, hbias=None, vbias=None, numpy_rng=None):

        self.input = input
        self.n_visible = n_visible
        self.n_hidden = n_hidden

        if numpy_rng is None:
            numpy_rng = numpy.random.RandomState(1234)  # 随机数生成numpy-rng

            # 参数为none后，初始化为 -4*sqrt(6./(n_visible+n_hidden))
        if W is None：
        W = numpy.asarray(numpy_rng.uniform(
            low=-4 * numpy.sqrt(6. / (n_hidden + n_visible)),
            high=4 * numpy.sqrt(6. / (n_hidden + n_visible)),
            size=(n_visible, n_hidden)))

        if hbias is None:
            hbias = numpy.zeros(n_hidden)  # 偏置项都设为0

        if vbias is None:
            vbias = numpy.zeros(n_visible)

        self.numpy_rng = numpy_rng
        self.W = W
        self.hbias = hbias
        self.vbias = vbias

    def propup(self, vis):  # 前向
        pre_sigmoid_activation = numpy.dot(vis, self.W) + self.hbias
        return sigmoid(pre_sigmoid_activation)

    def sample_h_given_v(self, v0_sample):  # 根据可视层v采样计算隐层h为1的状态
        h1_mean = self.propup(v0_sample)
        h1_sample = self.numpy_rng.binomial(
            size=h1_mean.shape, n=1, p=h1_mean)  # 只有0和1两种状态
        return [h1_mean, h1_sample]

    def propdown(self, hid):  # 后向
        pre_sigmoid_activation = numpy.dot(hid, self.W.T) + self.vbias
        return sigmoid(pre_sigmoid_activation)

    def sample_v_given_h(self, h0_sample):  # 根据隐层v采样计算可视层
        v1_mean = self.propdown(h0_sample)
        v1_sample = self.numpy_rng.binomial(size=v1_mean.shape, n=1, p=v1_mean)
        return [v1_mean, v1_sample]

    def gibbs_hvh(self, h0_sample):  # 整个Gibbs采样
        v1_mean, v1_sample = self.sample_v_given_h(h0_sample)  # v-h
        h1_mean, h1_sample = self.sample_h_given_v(v1_sample)  # h-v
        return [v1_mean, v1_sample,
                h1_mean, h1_sample]

    def get_cost_updates(self, lr=0.1, persistent=None, k=1):  # k为采样次数
        ph_mean, ph_sample = self.sample_h_given_v(
            self.input)  # 先根据输入input计算隐层的结果

        if persistent is None:
            chain_start = ph_sample
        else:
            chain_start = persistent

        for step in xrange(k):  # 计算k次
            if step == 0:
                nv_means, nv_samples,\
                    nh_means, nh_samples = self.gibbs_hvh(
                        chain_start)  # 拿到最后一次结束的状态
            else:
                nv_means, nv_samples,\
                    nh_means, nh_samples = self.gibbs_hvh(nh_samples)

        self.W += lr * (numpy.dot(self.input.T, ph_mean)
                        - numpy.dot(nv_samples.T, nh_means))
        self.vbias += lr * numpy.mean(self.input - nv_samples, axis=0)
        self.hbias += lr * numpy.mean(ph_mean - nh_means, axis=0)

        monitoring_cost = numpy.mean(
            numpy.square(self.input - nv_means))  # 损失函数
        return monitoring_cost


def load_data(dataset='mnist.pkl.gz'):
    dataset = os.path.join(os.path.split(__file__)[0], '../data', dataset)
    f = gzip.open(dataset, 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()

    def make_numpy_array(data_xy):
        data_x, data_y = data_xy
        return numpy.array(data_x), numpy.array(data_y)

    train_set_x, train_set_y = make_numpy_array(train_set)
    valid_set_x, valid_set_y = make_numpy_array(valid_set)
    test_set_x, test_set_y = make_numpy_array(test_set)

    rval = [(train_set_x, train_set_y), (valid_set_x, valid_set_y),
            (test_set_x, test_set_y)]

    return rval


def test(learning_rate=0.1, k=1, training_epochs=15):
    datasets = load_data('mnist.pkl.gz')  # 载入minst数据
    train_set_x, train_set_y = datasets[0]
    test_set_x, test_set_y = datasets[2]

    rbm = RBM(input=train_set_x, n_visible=28 * 28, n_hidden=500)

    start_time = time.clock()

    for epoch in xrange(training_epochs):
        cost = rbm.get_cost_updates(lr=learning_rate, k=k)
        print('Training epoch %d, cost is ' % epoch, cost)

    end_time = time.clock()
    pretraining_time = (end_time - start_time)

    print('Training took %f minutes' % (pretraining_time / 60.))


if __name__ == '__main__':
    test()
