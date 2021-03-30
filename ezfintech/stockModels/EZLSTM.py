import tensorflow as tf

class EZLSTM(tf.keras.layers.Layer):
    """
        Input: [batchSize，sequenceLength，inputSize]
        Output: [batchSize，sequenceLength，outputSize]
        Output2: [batchSize，sequenceLength]
    """
    
    def __init__(self,outputSize,returnSequence=False):
        super(EZ_LSTM,self).__init__()
        self.outputSize = outputSize
        self.returnSequence = returnSequence
        
    def build(self,inputShape):
        super(EZ_LSTM,self).build(inputShape)
        inputSize = int(inputShape[-1])
        self.wf = self.add_weight("wf",shape=(inputSize,self.outputSize))
        self.wi = self.add_weight("wi",shape=(inputSize,self.outputSize))
        self.wo = self.add_weight("wo",shape=(inputSize,self.outputSize))
        self.wc = self.add_weight("wc",shape=(inputSize,self.outputSize))
        
        self.uf = self.add_weight("uf",shape=(self.outputSize,self.outputSize))
        self.ui = self.add_weight("ui",shape=(self.outputSize,self.outputSize))
        self.uo = self.add_weight("uo",shape=(self.outputSize,self.outputSize))
        self.uc = self.add_weight("uc",shape=(self.outputSize,self.outputSize))

        self.bf = self.add_weight("bf",shape=(1,self.outputSize))
        self.bi = self.add_weight("bi",shape=(1,self.outputSize))
        self.bo = self.add_weight("bo",shape=(1,self.outputSize))
        self.bc = self.add_weight("bc",shape=(1,self.outputSize))
        
    def call(self,x):
        sequenceOutputs = []
        for i in range(sequenceLength):
            if i==0:
                xt = x[:,0,:]
                ft = tf.sigmoid(tf.matmul(xt,self.wf)+self.bf)
                it = tf.sigmoid(tf.matmul(xt,self.wi)+self.bi)
                ot = tf.sigmoid(tf.matmul(xt,self.wo)+self.bo)
                cht = tf.tanh(tf.matmul(xt,self.wc)+self.bc)
                ct = it * cht
                ht = ot *tf.tanh(ct)
            else:
                xt = x[:,0,:]
                ft = tf.sigmoid(tf.matmul(xt,self.wf)+tf.matmul(ht,self.uf)+self.bf)
                it = tf.sigmoid(tf.matmul(xt,self.wi)+tf.matmul(ht,self.ui)+self.bi)
                ot = tf.sigmoid(tf.matmul(xt,self.wo)+tf.matmul(ht,self.uo)+self.bo)
                cht = tf.tanh(tf.matmul(xt,self.wc)+tf.matmul(ht,self.uc)+self.bc)
                ct = ft*ct + it*cht
                ht = ot *tf.tanh(ct)
            sequenceOutputs.append(ht)
        sequenceOutputs = tf.stack(sequenceOutputs)
        sequenceOutputs = tf.transpose(sequenceOutputs,(1,0,2))
        if self.returnSequence:
            return sequenceOutputs
        else:
            return sequenceOutputs[:,-1,:]