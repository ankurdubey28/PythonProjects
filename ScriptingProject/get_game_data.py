import os
import shutil
import json
import subprocess
from subprocess import PIPE,run
import sys


GAME_DIR_PATTERN="game"
GAME_FILE_EXTENSION=".go"
GAME_COMPILE_COMMAND=["go","build"]

def compile_game_code(path):
   code_file_name=None
   for root,dir,files in os.walk(path):
       for file in files:
           if file.endswith(GAME_FILE_EXTENSION):
               code_file_name=file
               break

   if code_file_name==None:
       return

   command=GAME_COMPILE_COMMAND+[code_file_name]
   run_commmand(command, path)


def run_commmand(command,path):
    cwd=os.getcwd()
    os.chdir(path)

    res=run(command,stdout=PIPE,stdin=PIPE,universal_newlines=True)
    print(res)

    os.chdir(cwd)


def find_all_game_paths(src):
    game_paths=[]

    for root,dirs,files in os.walk(src):
       for directory in dirs:
           if GAME_DIR_PATTERN in directory.lower():
               path=os.path.join(src,directory)
               game_paths.append(path)
       break

    return game_paths



def get_name_from_path(paths,to_strip):
    new_names=[]
    for path in paths:
        _,dir_name=os.path.split(path)
        new_dir_name=dir_name.replace(to_strip,"")
        new_names.append(new_dir_name)
    return new_names



def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def copy_and_overwrite(src,dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src,dest)


def make_json_metadata_file(path,game_dirs):
    data={
        "gameNames":game_dirs,
        "numberOfGames":len(game_dirs)
    }
    with open(path,"w") as f:
        json.dump(data,f)



def main(src,tar):
    src_path=os.path.join(os.getcwd(),src)
    tar_path=os.path.join(os.getcwd(),tar)

    game_paths=find_all_game_paths(src)
    new_game_dirs=get_name_from_path(game_paths,"_game")
    create_dir(tar_path)
    for src,dest in zip(game_paths,new_game_dirs):
        dest_path=os.path.join(tar_path,dest)
        copy_and_overwrite(src,dest_path)
        compile_game_code(dest_path)

    json_path=os.path.join(tar_path,"metadata.json")
    make_json_metadata_file(json_path)


if __name__ == "__main__":
    args=sys.argv  # picks up argument from command line
    if len(args)!=3:
        raise Exception("Only target and source directory allowed .")
    src,targ=args[1:]
    main(src,targ)