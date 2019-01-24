import monkdata as m
import dtree as dt
import drawtree_qt5 as draw
import random

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

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


monk1train, monk1val = partition(m.monk1, 0.6)

currentTree = dt.buildTree(dataset=monk1train, attributes=m.attributes)

original = currentTree
treeCopy = currentTree
best = currentTree
notdone = True

while notdone:
    #print("looking")
    treeCopy = best
    array = dt.allPruned(treeCopy)
    print("new array")
    for i in array:
        print("new candidate")
        if dt.check(i, monk1val)>dt.check(best, monk1val):
            best = i
            print("bigger", dt.check(i, monk1val), " ", dt.check(best, monk1val))
        else:
            print("lesser", dt.check(i, monk1val), " ", dt.check(best, monk1val))

    if currentTree == best:
        print("no new best found. quitting")
        notdone = False
    else:
        print("replacing best")
        currentTree = best

#draw.drawTree(original)
draw.drawTree(currentTree)