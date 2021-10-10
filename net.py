
from tensorflow.keras.layers import(
Input , Conv1D,MaxPool1D,concatenate,add,BatchNormalization, GlobalAveragePooling2D,Flatten,Dense,ReLU
)
from tensorflow.keras.models import Model



def convPool(filters, kernel_size, strides=1, padding='same', pool_size=2):
    def layer (x):
        conv = Conv1D(int(filters),kernel_size, strides, padding)(x)
        conv = BatchNormalization()(conv)
        pool = MaxPool1D(pool_size, strides=pool_size, padding='same')(conv)
        return pool
    return layer


def make_net(input_shape):
    sample =Input(shape = input_shape)
    #v0.1
    conv1 = convPool(filters=16, kernel_size=3)(sample)
    conv2 = convPool(filters=32, kernel_size=3)(conv1)

    flat = Flatten()(conv2)

    dens1 = Dense(units = 120, activation=None)(flat)
    dens1 = BatchNormalization()(dens1)

    dens2 = Dense(units=120 , activation=None)(dens1)
    dens2 = BatchNormalization()(dens2)
    dens2 = ReLU()(dens2)

    densSigmoid = Dense(units=181, activation='sigmoid', name='out1')(dens2)
    densReLu = Dense(units=181, activation='relu', name='out2')(dens2)

    #out = concatenate([densSigmoid,densReLu])

    model =  Model(inputs = [sample], outputs=[densSigmoid, densReLu] )
    return model

