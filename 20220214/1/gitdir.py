import sys, zlib
from os import listdir
from os.path import join, exists

PATH_GIT_BRANCHES = '.git/refs/heads/'
PATH_GIT_OBJECTS = '.git/objects/'
BYTE_SEP = b'\x00'
SHIFT = "  "

def git_tree_show_as_tree(tree_name,lvl = 1):

    tree_dir, tree_file = tree_name[:2]+'/', tree_name[2:]
    tree_file_path = join(PATH_GIT_OBJECTS,tree_dir,tree_file)

    with open(tree_file_path, 'rb') as f_tree:
        f_text = zlib.decompress(f_tree.read())
    head, _, tail = f_text.partition(BYTE_SEP)
    kind, size = head.split()
    
    if kind != b'tree':
        if (lvl < 2):
            print(f"Это не дерево {tree_name}")
        return
    
    while tail:
        head, _, tail = tail.partition(b'\x00')
        tre_mode, tre_name = head.split()

        num, tail = tail[:20], tail[20:]
        print(f"{SHIFT*lvl}{tre_name.decode()} {tre_mode.decode()} {num.hex()}")
        git_tree_show_as_tree(num.hex(), lvl + 1)

def git_tree_show(tree_name):

    tree_dir, tree_file = tree_name[:2]+'/', tree_name[2:]
    tree_file_path = join(PATH_GIT_OBJECTS,tree_dir,tree_file)

    with open(tree_file_path, 'rb') as f_tree:
        f_text = zlib.decompress(f_tree.read())
    tail = f_text.partition(BYTE_SEP)[-1]
    
    while tail:
        head, _, tail = tail.partition(BYTE_SEP)
        tre_mode, tre_name = head.split()
        num, tail = tail[:20], tail[20:]
        print(f"{SHIFT}{tre_name.decode()} {tre_mode.decode()} {num.hex()}")


def pass_tre_comits(commit_name):
    commit_name_dir, commit_name_file = commit_name[:2] +'/', commit_name[2:]
    commit_file_path = join(PATH_GIT_OBJECTS,commit_name_dir,commit_name_file)
    
    with open(commit_file_path, 'rb') as obj_file:
        commit = zlib.decompress(obj_file.read()).decode()
    
    print(commit)

    parent = commit.split("parent")
    
    if (len(parent) < 2):
        print("END")
        return
    parent =parent[1].split('\n')[0].strip()
    pass_tre_comits(parent)





def branch_history_show(branch_name):
    branch_path = join(PATH_GIT_BRANCHES,branch_name) 
    if  not exists(branch_path):
        print(f"Нет такой ветки или пути {branch_path}")
        return

    with open(branch_path) as f_branch:
        f_text = f_branch.readline()
    
    commit_name = f_text.strip()

    pass_tre_comits(commit_name) 

    



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
    
    git_tree_show(commit_tree_name)

    git_tree_show_as_tree(commit_tree_name)

    branch_history_show(branch_name[0])



    

if ( __name__ == '__main__'):
    if len(sys.argv) > 1:
        git_branches_show(sys.argv[1])
    else:
        git_branches_show()
