use std::cmp::max;
use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug)]
struct TreeNode {
    val: i32,
    left: Option<Rc<RefCell<TreeNode>>>,
    right: Option<Rc<RefCell<TreeNode>>>,
}

fn dfs(node: &Option<Rc<RefCell<TreeNode>>>) -> (i32, bool) {
    match node {
        None => (0, true),
        Some(n) => {
            let n = n.borrow();
            let (lh, lb) = dfs(&n.left);
            let (rh, rb) = dfs(&n.right);

            let height = 1 + max(lh, rh);
            let balanced = lb && rb && (lh - rh).abs() <= 1;

            (height, balanced)
        }
    }
}

fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
    dfs(&root).1
}
