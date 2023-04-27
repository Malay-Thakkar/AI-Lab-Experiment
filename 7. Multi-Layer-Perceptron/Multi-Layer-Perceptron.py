from numpy import dot


class perceptronNeuron:
    def __init__(self, x, w, w0):
        l = [ww for ww in x]
        l.insert(0, 1)
        self.x = l
        self.y = 0
        l = [ww for ww in w]
        l.insert(0, w0)
        self.w = l
        #print("L:"+str(l)+", w:"+str(w)+"self.w:"+str(self.w))

    def __repr__(self):
        return "Input:"+str(self.x)+", Weight:"+str(self.w)

    def activationFunction(self):
        self.y = 1 if dot(self.x, self.w) >= 0 else 0
        return self.y

    def dot(x, W):
        if len(x) != len(W):
            return 0
        return sum(i[0] * i[1] for i in zip(X, W))


class multiLayerPerceptron:
    def __init__(self, a0, a1, dimension, inputBias, weight, functionName, s0, s1):
        self.n = dimension
        self.a0 = a0
        self.a1 = a1
        self.inputBias = inputBias
        self.hidden = []
        self.weight = weight
        self.funcName = functionName
        self.s0 = s0
        self.s1 = s1

    def binaryCombinations(self, a0, a1, n):
        list1 = []
        for i in range(1 << n):
            s = bin(i)[2:]
            s = '0'*(n-len(s))+s
            l = list(map(int, list(s)))
            l = [a0 if item == 0 else a1 for item in l]
            list1.append(l)
        return list1

    def generateHiddenLayer(self, input):
        allPossibleList = self.binaryCombinations(self.a0, self.a1, self.n)
        self.hidden = [perceptronNeuron(input, weight, self.inputBias)
                       for weight in allPossibleList]
        return self.hidden

    def outputActivationFun(self, hiddenLayer):
        return self.a1 if dot(hiddenLayer, self.weight) >= 0 else self.a0

    def generateOutput(self, xStr):
        allPossibleInputs = self.binaryCombinations(self.a0, self.a1, self.n)
        output = []
        strheader = "\n"+self.funcName+"\n"
        for i in range(self.n):
            strheader += (xStr+str(i+1)+"\t")
        strheader += ("Output")
        print(strheader)
        for input in allPossibleInputs:
            allhiddenOutput = self.generateHiddenLayer(input)
            # print(allhiddenOutput)
            o = [hiddenPerceptron.activationFunction()
                 for hiddenPerceptron in allhiddenOutput]
            o.insert(0, 1)
            # print(str(o))
            o = self.outputActivationFun(o)
            output.append(o)
            print(str([self.s0 if item == self.a0 else self.s1 for item in input]).replace("[", "").replace(
                "]", "").replace(",", "\t").replace("'", "")+"\t"+str(self.s0 if o == self.a0 else self.s1))


# return output
true = 1
false = -1
initialBias = -2
outputBias = -1
dimension = 2
s0 = "0"
s1 = "1"
xStr = "x"
andMLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                              outputBias, false, false, false, true], "AND Function", s0, s1)
orMLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                             outputBias, false, true, true, true], "OR Function", s0, s1)
xorMLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                              outputBias, false, true, true, false], "XOR Function", s0, s1)
xnorMLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                               outputBias, true, false, false, true], "XNOR Function", s0, s1)
norMLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                              outputBias, true, false, false, false], "NOR Function", s0, s1)
nandMLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                               outputBias, true, true, true, false], "NAND Function", s0, s1)
notInput1MLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                                    outputBias, true, true, false, false], "Not"+xStr+"1 Function", s0, s1)
notInput2MLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                                    outputBias, true, false, true, false], "Not"+xStr+"2 Function", s0, s1)
nullMLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                               outputBias, false, false, false, false], "NULL Function", s0, s1)
identityMLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                                   outputBias, true, true, true, true], "Identity Function", s0, s1)
inhibition1MLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                                      outputBias, false, false, true, false], "Inhibition x1^~x2 Function", s0, s1)
inhibition2MLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                                      outputBias, false, true, false, false], "Inhibition x2^~x1 Function", s0, s1)
transferX1MLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                                     outputBias, false, false, true, true], "Transfer x1 Function", s0, s1)
transferX2MLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                                     outputBias, false, true, false, true], "Transfer x2 Function", s0, s1)
implication1MLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                                       outputBias, true, false, true, true], "Implication x1V~x2 Function", s0, s1)
implication2MLP = multiLayerPerceptron(false, true, dimension, initialBias, [
                                       outputBias, true, true, false, true], "Implication x2V~x1 Function", s0, s1)
andMLP.generateOutput(xStr)
orMLP.generateOutput(xStr)
xorMLP.generateOutput(xStr)
norMLP.generateOutput(xStr)
xnorMLP.generateOutput(xStr)
nandMLP.generateOutput(xStr)
notInput1MLP.generateOutput(xStr)
notInput2MLP.generateOutput(xStr)
nullMLP.generateOutput(xStr)
identityMLP.generateOutput(xStr)
inhibition1MLP.generateOutput(xStr)
inhibition2MLP.generateOutput(xStr)
transferX1MLP.generateOutput(xStr)
transferX2MLP.generateOutput(xStr)
implication1MLP.generateOutput(xStr)
implication2MLP.generateOutput(xStr)
