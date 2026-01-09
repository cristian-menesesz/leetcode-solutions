use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

pub struct Solution {
    global_max_depth: i32,
}

impl Solution {
    pub fn subtree_with_all_deepest(
        root: Option<Rc<RefCell<TreeNode>>>
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let mut s = Solution { global_max_depth: 0 };
        let (node, _) = s.dfs(root, 0);
        node
    }

    fn dfs(
        &mut self,
        node: Option<Rc<RefCell<TreeNode>>>,
        current_depth: i32,
    ) -> (Option<Rc<RefCell<TreeNode>>>, i32) {
        match node {
            None => {
                self.global_max_depth = self.global_max_depth.max(current_depth);
                (None, current_depth)
            }
            Some(n) => {
                let left = self.dfs(n.borrow().left.clone(), current_depth + 1);
                let right = self.dfs(n.borrow().right.clone(), current_depth + 1);

                if left.1 == right.1 && left.1 == self.global_max_depth {
                    (Some(n), left.1)
                } else if left.1 > right.1 {
                    left
                } else {
                    right
                }
            }
        }
    }
}
