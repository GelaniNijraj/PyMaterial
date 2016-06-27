from MBase.MValueAnimator import MValueAnimator

# Going from 0 to 100 in 1000ms at 60 fps
value_animator = MValueAnimator(0, 100, 1000, 60)

try:
    while(True):
        print(value_animator.step())
except OverflowError:
    print("Completed")

# value_animator = MValueAnimator(0, 1, 1000, 100)
#
# try:
#     while(True):
#         value_animator.step()
# except OverflowError:
#     print("Completed")
