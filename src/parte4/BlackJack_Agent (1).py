import gym
import numpy as np
import matplotlib.pyplot as plt
from QLearning_BlackJack import QLearning
from numpy import loadtxt

env = gym.make('Blackjack-v1')
i = 0.01
g = 0.1
epi = 700000

qlearn = QLearning(env, alpha=i, gamma=g, epsilon=0.9,epsilon_min=0.01, epsilon_dec=0.99, episodes=epi)
#q_table = qlearn.train('data/q-table-blackjack.csv', None)
q_table = loadtxt('data/q-table-blackjack.csv', delimiter=',')

state= env.reset()
done = False

while not done:
    print(state)
    n_state = QLearning.stateNumber(state)
    action = np.argmax(q_table[n_state])
    state, reward, done, info = env.step(action)
    print(f' Jogando: {action}')
    
print(f' Cartas do meu jogador: {env.player}')
print(f' Cartas do dealer: {env.dealer}')

if reward == 1:
    print('Meu jogador venceu')
elif reward == 0:
    print('Jogo empatou')
elif reward == -1:
    print('Dealer ganhou')