import sys, zlib
from os import listdir
from os.path import join, exists

PATH_GIT_BRANCHES = '.git/refs/heads/'
PATH_GIT_OBJECTS = '.git/objects/'
BYTE_SEP = b'\x00'
SHIFT = "  "

def git_branches_show (*branch_name):
    if not branch_name:
        for branch in listdir(PATHGITBRANCHES):
            print(branch)
        return    
    
    branch_path = join(PATH_GIT_BRANCHES,branch_name[0]) 
    if  not exists(branch_path):
        print(f"Нет такой ветки или пути {branch_path}")
        return

    with open(branch_path) as f_branch:
        f_text = f_branch.readline()
    
    f_text = f_text.strip()
    commit_name_dir, commit_name_file = f_text[:2] +'/', f_text[2:]
    commit_file_path = join(PATH_GIT_OBJECTS,commit_name_dir,commit_name_file)
    
    with open(commit_file_path, 'rb') as obj_file:
        commit = zlib.decompress(obj_file.read()).decode()
    
    print(commit)

    commit_tree_name = commit.split('\n')[0].split('tree')[1].strip()
    tree_dir, tree_file = commit_tree_name[:2]+'/', commit_tree_name[2:]
    tree_file_path = join(PATH_GIT_OBJECTS,tree_dir,tree_file)

    with open(tree_file_path, 'rb') as f_tree:
        f_text = zlib.decompress(f_tree.read())
    tail = f_text.partition(BYTE_SEP)[-1]
    
    while tail:
        head, _, tail = tail.partition(BYTE_SEP)
        tre_mode, tre_name = head.split()
        num, tail = tail[:20], tail[20:]
        print(f"{SHIFT}{tre_name.decode()} {tre_mode.decode()} {num.hex()}")
     



    

if ( __name__ == '__main__'):
    if len(sys.argv) > 1:
        git_branches_show(sys.argv[1])
    else:
        git_branches_show()