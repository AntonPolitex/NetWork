from  tensorflow.keras.optimizers import Adam
from net import make_net
from gen import Generator
from tensorflow.keras.losses import logcosh
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau,LearningRateScheduler
from albumentations import(
 HorizontalFlip,VerticalFlip,ShiftScaleRotate,Compose,OneOf
)


model = make_net((801,3))
model.compile(optimizer=Adam(3e-4), loss= {'out1':'binary_crossentropy', 'out2':'mae'}, metrics= ['accuracy', 'mae'])

train_gen = Generator('/home/user-104/PycharmProjects/Troshintest/Сетка/pathFilse.csv',(801,3),3,None)
val_gen = Generator('/home/user-104/PycharmProjects/Troshintest/Сетка/pathFilse.csv',(801,3),1,None)
def sheduler(epoch,lr):
    if epoch > 1:
       lr = lr*0.95
    return lr



callbaks =[
    ModelCheckpoint('/home/user-104/PycharmProjects/Troshintest/Сетка/TrainToDream/mashina_val_good.h5',
                    monitor= 'val_loss',
                    verbose= 1,
                    save_best_only= True,
                    save_weights_only= False,
                    mode='min'),
   #LearningRateScheduler(sheduler),
   #ReduceLROnPlateau(monitor='val_loss',
   #                  mode='min',
   #                  patience=5,
   #                  verbose=1,
   #                  factor=0.5)
]
model.fit(train_gen,validation_data= val_gen , epochs= 10000 ,verbose = 1,callbacks = callbaks)