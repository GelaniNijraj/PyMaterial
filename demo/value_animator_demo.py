from MBase import *

# Going from 0 to 100 in 1000ms at 60 fps
value_animator = MValueAnimator(1, 0, 1000, 60)

try:
    while(True):
        print(value_animator.step())
except MFinalValueReachedException:
    print("Completed")

# value_animator = MValueAnimator(0, 1, 1000, 100)
#
# try:
#     while(True):
#         value_animator.step()
# except OverflowError:
#     print("Completed")
