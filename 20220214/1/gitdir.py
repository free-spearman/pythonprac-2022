import sys, zlib
from os import listdir
from os.path import join

PATHGITBRANCHES = '.git/refs/heads/'
PATHGITOBJECTS = '.git/objects/'

def git_branches_show (*branch_name):
    if not branch_name:
        for branch in listdir(PATHGITBRANCHES):
            print(branch)
        return    
    
    branch_path = join(PATHGITBRANCHES,branch_name[0]) 
    with open(branch_path) as f_branch:
        f_text = f_branch.readline()
    
    f_text = f_text.strip()
    commit_name_dir, commit_name_file = f_text[:2] +'/', f_text[2:]
    commit_file_path = join(PATHGITOBJECTS,commit_name_dir,commit_name_file)
    
    with open(commit_file_path, 'rb') as obj_file:
        commit = zlib.decompress(obj_file.read()).decode()
    
    print(commit)


if ( __name__ == '__main__'):
    if len(sys.argv) > 1:
        git_branches_show(sys.argv[1])
    else:
        git_branches_show()