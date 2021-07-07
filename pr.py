q="y"
b=""
while(q=="y"):
    def binary_tree(x):
        return [x,[],[]]
    def insert_left(root,new_branch):
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1,[new_branch,t,[]])
        else:
            root.insert(1,[new_branch,[],[]])
        return root
    def insert_right(root,new_branch):
        t=root.pop(2)
        if len(t) > 1:
            root.insert(2,[new_branch,[],t])
        else:
            root.insert(2,[new_branch,[],[]])
        return root
    def get_root_val(root):
        return root[0]
    def set_root_val(root,new_val):
        root[0]=new_val
    def get_left_child(root):
        return root[1]
    def get_right_child(root):
        return root[2]

    b=str(input("cuaca :"))
    x=binary_tree(b)
    insert_left(x, input(str("akar :")))
    insert_left(x, input(str("pohon :")))
    insert_right(x, input(str("cabang kiri :")))
    insert_right(x, input(str("cabang kanan :")))
    i = get_left_child(x)

    print(x)
    if (x=="hujan")or(x=="angin"):
        print("hasil : tidak main")
    elif (x=="cerah") or (x=="lembab"):
        print("hasil : bisa main")


    q = input("mau ulang : [y/n]")