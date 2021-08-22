import schedule
import time
import os


def shutdown(shut):
    if shut == 'no':
        exit()
    else:
        os.system("shutdown /s /t 1")


# Task scheduling
# After every 10mins
schedule.every(10).minutes.do(shutdown('no'))

# After every hour
schedule.every().hour.do(shutdown('no'))

# Every day at 12am or 00:00
schedule.every().day.at("00:00").do(shutdown('yes'))

# After every 5 to 10mins
schedule.every(5).to(10).minutes.do(shutdown('no'))

# Every monday
schedule.every().monday.do(shutdown('no'))

# Every tuesday at 18:00
schedule.every().tuesday.at("18:00").do(sudo_placement)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
