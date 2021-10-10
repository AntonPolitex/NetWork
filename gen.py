import csv
import numpy as np
from tensorflow.keras.utils import Sequence


class Generator (Sequence):
    def __init__(self,ann_path, sample_shape ,batch_size,augs):
        super(Generator,self).__init__()
        self.ann_path = ann_path  # путь к файлу, в которой есть все нужные путь О для тренировки,1 для теста
        self.sample_shape = sample_shape # тут размеры сэмпла (801 на 3)
        self.batsh_size = batch_size
        self.augs = augs
        self.annotations = []
        with open(self.ann_path) as f:  # открываем проверяющий файл и запихиваем в аннтотации
            reader = csv.reader(f)
            for j, row in enumerate(reader):
                self.annotations.append(row)
            f.close()

    def __len__(self):
        return len(self.annotations) // self.batsh_size

    def __getitem__ (self,idx):
        batch = self.annotations[idx*self.batsh_size: (idx+1) * self.batsh_size] # батч для сэмплов
        self.sample_shape  = (801, 3)      # если будешь менять размеры семпла не забудь изменить и тут

        samples = np.empty((self.batsh_size, self.sample_shape[0], self.sample_shape[1]), np.float32)
        labelsigm = np.zeros((self.batsh_size,181, 1), np.float32)
        labelsrel = np.zeros((self.batsh_size, 181, 1), np.float32)
        for i, ann in enumerate(batch):
            sample = np.zeros((801, 3), np.float32)
            with open(ann[0]) as f: #открываем сепл файл и записываем данные в семпл
                reader = csv.reader(f)
                for j, row in enumerate(reader):
                    sample[j, 0] = float(row[0])
                    sample[j, 1] = float(row[1])
                    sample[j, 2] = float(row[2])
            samples[i] = sample

            with open(ann[1], 'r') as f:
                labelsig = np.zeros((181, 1), np.float32)
                labelrel = np.zeros((181, 1), np.float32)
                for j, line in enumerate(f):
                        line = line.strip()
                        if len(line) < 3:
                            continue
                        lst = line.split(",")
                        labelsig[j] = float(lst[1])
                        labelrel[j] = float(lst[2])
                labelsigm[i] = labelsig
                labelsrel[i] = labelrel

        return samples, {'out1':labelsigm, 'out2' : labelsrel}

#a= Generator('/home/user-104/PycharmProjects/Troshintest/Сетка/pathFilse.csv',(801,3) ,1,None)
#print(a.__getitem__(68))



