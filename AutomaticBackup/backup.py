import os
import shutil
import datetime
import schedule
import time

source_dir="C:/Users/ankur/JSProjects"
destination_dir="C:/Users/ankur/backups"


def copy_folder_to_dir(source,dest):
    today = datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    dest_dir=os.path.join(dest,str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"folder copied ")
    except FileExistsError:
        print(f"Folder already exists in :{dest}")

schedule.every().day.at("18:55").do(lambda :copy_folder_to_dir(source_dir,destination_dir))


while True:
    schedule.run_pending()
    time.sleep(60)