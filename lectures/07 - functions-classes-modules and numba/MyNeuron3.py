import numpy as np
import MyNeuron


brainRegion = "hippocampus"


def createThreeRandomNeurons():
    randomSpikeRatesPerSec = 10 / np.random.random(3)
    neurons = []
    for rate in randomSpikeRatesPerSec:
        neurons.append(MyNeuron.MySpikingNeuron(rate))
    return neurons