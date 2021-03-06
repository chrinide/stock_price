import sys
from data.stock import Stock
from predictor import Predictor
from score import auc
from preprocess import Preprocess

submission_number = sys.argv[1]
print submission_number 

def submission(ids, preds):
    name = "submissions/submission{0}.csv".format(submission_number)
    f = open(name, 'w')
    if len(ids) != len(preds):
        raise Exception("The number of IDs and the number of predictions are different")
    string = 'id,prediction\n'
    for index,i in enumerate(ids):
        string += str(i) + ',' + str(preds[index]) + "\n"
    f.write(str(string))
    f.close()

data, targets, _ = Stock.train()
holdout_data, ids = Stock.test()
assert len(data) == len(targets)

Predictor.train(data, targets)
preds = Predictor.multi_predict(holdout_data)
print preds[0:50]
submission(ids, preds)
