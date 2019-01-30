import monkdata as m
import dtree as dt
import drawtree_qt5 as draw
import random
import matplotlib.pyplot as plot
import matplotlib.patches as mpatches

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def getMin(list):
    min = 1
    for l in list:
        if l < min:
            min = l
    return min

def getMax(list):
    max = 0
    for l in list:
        if l > max:
            max = l
    return max

def getAvg(list):
    sum = 0
    for l in list:
        sum+=l;

    sum = sum/1000
    return sum

print(dt.entropy(m.monk1))
print(dt.entropy(m.monk2))
print(dt.entropy(m.monk3))

print("gains")
print("monk1")
print("0", dt.averageGain(m.monk1, m.attributes[0]))
print("1", dt.averageGain(m.monk1, m.attributes[1]))
print("2", dt.averageGain(m.monk1, m.attributes[2]))
print("3", dt.averageGain(m.monk1, m.attributes[3]))
print("4", dt.averageGain(m.monk1, m.attributes[4]))
print("5", dt.averageGain(m.monk1, m.attributes[5]))

print("monk2")
print("0", dt.averageGain(m.monk2, m.attributes[0]))
print("1", dt.averageGain(m.monk2, m.attributes[1]))
print("2", dt.averageGain(m.monk2, m.attributes[2]))
print("3", dt.averageGain(m.monk2, m.attributes[3]))
print("4", dt.averageGain(m.monk2, m.attributes[4]))
print("5", dt.averageGain(m.monk2, m.attributes[5]))

print("monk3")
print("0", dt.averageGain(m.monk3, m.attributes[0]))
print("1", dt.averageGain(m.monk3, m.attributes[1]))
print("2", dt.averageGain(m.monk3, m.attributes[2]))
print("3", dt.averageGain(m.monk3, m.attributes[3]))
print("4", dt.averageGain(m.monk3, m.attributes[4]))
print("5", dt.averageGain(m.monk3, m.attributes[5]))

list1 = dt.select(m.monk1, m.attributes[4], 1)
list2 = dt.select(m.monk1, m.attributes[4], 2)
list3 = dt.select(m.monk1, m.attributes[4], 3)
list4 = dt.select(m.monk1, m.attributes[4], 4)

print("gains")
print("list1")
print("0", dt.averageGain(list1, m.attributes[0]))
print("1", dt.averageGain(list1, m.attributes[1]))
print("2", dt.averageGain(list1, m.attributes[2]))
print("3", dt.averageGain(list1, m.attributes[3]))
print("5", dt.averageGain(list1, m.attributes[5]))
print("list2")
print("0", dt.averageGain(list2, m.attributes[0]))
print("1", dt.averageGain(list2, m.attributes[1]))
print("2", dt.averageGain(list2, m.attributes[2]))
print("3", dt.averageGain(list2, m.attributes[3]))
print("5", dt.averageGain(list2, m.attributes[5]))
print("list3")
print("0", dt.averageGain(list3, m.attributes[0]))
print("1", dt.averageGain(list3, m.attributes[1]))
print("2", dt.averageGain(list3, m.attributes[2]))
print("3", dt.averageGain(list3, m.attributes[3]))
print("5", dt.averageGain(list3, m.attributes[5]))
print("list4")
print("0", dt.averageGain(list4, m.attributes[0]))
print("1", dt.averageGain(list4, m.attributes[1]))
print("2", dt.averageGain(list4, m.attributes[2]))
print("3", dt.averageGain(list4, m.attributes[3]))
print("5", dt.averageGain(list4, m.attributes[5]))


common = dt.mostCommon(dt.select(list4, m.attributes[0], 1))
common2 = dt.mostCommon(dt.select(list4, m.attributes[0], 2))
common3 = dt.mostCommon(dt.select(list4, m.attributes[0], 3))

print("attribute val 1 is mostly ", common)
print("attribute val 2 is mostly ", common2)
print("attribute val 3 is mostly ", common3)

t1 = dt.buildTree(dataset=m.monk1, attributes=m.attributes)
#t1 = dt.buildTree(dataset=m.monk1, attributes=m.attributes, maxdepth=5)
#draw.drawTree(t1)

t1 = dt.buildTree(dataset=m.monk1, attributes=m.attributes)
t2 = dt.buildTree(dataset=m.monk2, attributes=m.attributes)
t3 = dt.buildTree(dataset=m.monk3, attributes=m.attributes)

print("test")
print("monk1 training ", dt.check(t1, m.monk1))
print("monk1 test ", dt.check(t1, m.monk1test))

print("monk2 training ", dt.check(t2, m.monk2))
print("monk2 test ", dt.check(t2, m.monk2test))

print("monk3 training ", dt.check(t3, m.monk3))
print("monk3 test ", dt.check(t3, m.monk3test))

#result = []
fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.9]

result03 = []
result04 = []
result05 = []
result06 = []
result07 = []
result09 = []

testtrain, testval = partition(m.monk1, 0.9)
print("train", testtrain)
print("val", testval)

#result = [[] for _ in range(6)]
current = 0
for frac in fractions:


    for j in range(0,1000):
        #print("j", j)
        #monk1train, monk1val = partition(m.monk1, frac)
        #currentTree = dt.buildTree(dataset=monk1train, attributes=m.attributes)
        monk3train, monk3val = partition(m.monk3, frac)


        currentTree = dt.buildTree(dataset=monk3train, attributes=m.attributes)

        original = currentTree
        treeCopy = currentTree
        best = currentTree
        notdone = True

        while notdone:
            #print("looking")
            treeCopy = best
            array = dt.allPruned(treeCopy)
            #print("new array")
            for i in array:
                #print("new candidate")
                if dt.check(i, monk3val)>dt.check(best, monk3val):
                    best = i
                    #print("bigger", dt.check(i, monk1val), " ", dt.check(best, monk1val))
                #else:
                    #print("lesser", dt.check(i, monk1val), " ", dt.check(best, monk1val))

            if currentTree == best:
                #print("no new best found. quitting")
                notdone = False
            else:
                #print("replacing best")
                currentTree = best

        #print("frac ", frac, "error ", (1-dt.check(currentTree, m.monk1test)))
        if current < 1:
            result03.append(1-dt.check(currentTree, m.monk3test))
        elif current < 2:
            result04.append(1 - dt.check(currentTree, m.monk3test))
        elif current < 3:
            result05.append(1 - dt.check(currentTree, m.monk3test))
        elif current < 4:
            result06.append(1 - dt.check(currentTree, m.monk3test))
        elif current < 5:
            result07.append(1 - dt.check(currentTree, m.monk3test))
        elif current < 6:
            #print("adding to 09 current",  current)
            result09.append(1 - dt.check(currentTree, m.monk3test))

    current+=1

#print("result 03", result03)
#print("result 04", result04)
#print("result 05", result05)
#print("result 06", result06)
#print("result 07", result07)
#print("result 09", result09)

min = []
max = []
avg = []

min.append(getMin(result03))
min.append(getMin(result04))
min.append(getMin(result05))
min.append(getMin(result06))
min.append(getMin(result07))
min.append(getMin(result09))

max.append(getMax(result03))
max.append(getMax(result04))
max.append(getMax(result05))
max.append(getMax(result06))
max.append(getMax(result07))
max.append(getMax(result09))

avg.append(getAvg(result03))
avg.append(getAvg(result04))
avg.append(getAvg(result05))
avg.append(getAvg(result06))
avg.append(getAvg(result07))
avg.append(getAvg(result09))

print("min", min)
print("max", max)
print("avg", avg)

plot.axis([0,1,0,0.4])
m1plot = plot.plot(fractions, avg, 'go', label="monk3avg")
m1plotmin = plot.plot(fractions, min, 'ro', label="monk3min")
m1plotmax = plot.plot(fractions, max, 'bo', label="monk3max")

plot.xlabel("Fraction")
plot.ylabel("Test Data Error")
red = mpatches.Patch(color='red', label="Monk3 min")
green = mpatches.Patch(color='green', label="Monk3 avg")
blue = mpatches.Patch(color='blue', label="Monk3 max")
plot.legend(handles=[red, green, blue])
plot.show()
#draw.drawTree(original)
#draw.drawTree(currentTree)

