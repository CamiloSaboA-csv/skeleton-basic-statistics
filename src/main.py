from core.statistics import DataCapture

capture = DataCapture()


capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

# capture.add(6)
# capture.add(6)
# capture.add(6)
# capture.add(6)
# capture.add(9)
# capture.add(9)
# capture.add(9)
# capture.add(11)
# capture.add(2)
# capture.add(2)
# capture.add(2)
# # capture.add(0)
# # capture.add(0)
stats = capture.build_stats()

print(stats.less(999))
print(stats.between(3, '6'))
print(stats.greater(4))
#print(stats)


