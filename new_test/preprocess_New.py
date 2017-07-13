from cal_dis import cal_dis
from train_item_beat import item_beat
from find_Neighbour import find_Neighbour
from find_observed_rank import find_observed_rank
from cal_freq import cal_freq


def preprocess_new(num, beta, K):
    freq = cal_freq(num)
    find_observed_rank(num, K, freq)
    cal_dis(num)
    find_Neighbour(num, beta)
    item_beat(num)
