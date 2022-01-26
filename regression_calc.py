import math

import statics


def sigmoid(sentence_vec: list, weight_vec: list):
    z = 0
    bias = weight_vec[-1]
    for i in range(len(sentence_vec)):
        z += sentence_vec[i] * weight_vec[i]
    z += bias
    return 1 / (1 + math.pow(math.e, -z))


# def cost(res_sigmoid, res_real):
#     return -(res_real * math.log(math.e, res_sigmoid) + (1 - res_real) * math.log(math.e, 1 - res_sigmoid))


def update_weights(sentence_vec: list, weight_vec: list, res_sigmoid: float, important: bool):
    rate = statics.LEARNING_RATE
    print("Result: ", res_sigmoid)
    print("True:   ", important)
    print("Diff:   ", abs(res_sigmoid - important))
    change_vec = [(res_sigmoid - important) * sentence_vec[i] for i in range(len(sentence_vec))]
    change_vec.append(res_sigmoid - important)
    new_weights = [weight_vec[i] - rate * change_vec[i] for i in range(len(weight_vec))]
    return new_weights
