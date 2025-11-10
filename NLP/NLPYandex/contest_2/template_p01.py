import numpy as np


def softmax(vector):
    nice_vector = vector - vector.max()
    exp_vector = np.exp(nice_vector)
    exp_denominator = np.sum(exp_vector, axis=1)[:, np.newaxis]
    softmax_ = exp_vector / exp_denominator
    return softmax_


def multiplicative_attention(decoder_hidden_state, encoder_hidden_states, W_mult):
    st1 = np.dot(decoder_hidden_state.T, W_mult)
    st2 = np.dot(st1, encoder_hidden_states)
    attention_scores = softmax(st2)
    attention_vector = np.dot(attention_scores, encoder_hidden_states.T)
    return attention_vector.T


def additive_attention(decoder_hidden_state, encoder_hidden_states, v_add, W_add_enc, W_add_dec):
    W_enc_h = np.dot(W_add_enc, encoder_hidden_states)
    W_dec_s = np.dot(W_add_dec, decoder_hidden_state)
    tanh_input = np.tanh(W_enc_h + W_dec_s)
    e = np.dot(v_add.T, tanh_input)
    alpha = np.exp(e) / np.sum(np.exp(e))
    attention_vector = np.dot(encoder_hidden_states, alpha.T)
    return attention_vector
