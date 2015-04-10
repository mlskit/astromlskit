from pyroc import *
random_sample  = random_mixture_model()
print random_sample
roc = ROCData(random_sample)
roc.auc()
roc.plot(title='ROC Curve')
