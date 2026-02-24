#[derive(Debug)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Box<TreeNode>>,
    pub right: Option<Box<TreeNode>>,
}

pub struct Solution;

impl Solution {
    pub fn sum_root_to_leaf(root: Option<Box<TreeNode>>) -> i32 {
        fn dfs(node: &Option<Box<TreeNode>>, current_value: i32) -> i32 {
            match node {
                None => 0,
                Some(n) => {
                    // Shift bits and append current bit
                    let current_value = (current_value << 1) | n.val;

                    // Leaf node
                    if n.left.is_none() && n.right.is_none() {
                        return current_value;
                    }

                    dfs(&n.left, current_value)
                        + dfs(&n.right, current_value)
                }
            }
        }

        dfs(&root, 0)
    }
}