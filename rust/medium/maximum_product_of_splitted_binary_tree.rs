use std::cell::RefCell;
use std::rc::Rc;

const MOD: i64 = 1_000_000_007;

#[derive(Debug)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

struct Solution {
    max_product: i64,
    total_tree_sum: i64,
}

impl Solution {
    fn compute_subtree_sum(
        &mut self,
        node: Option<Rc<RefCell<TreeNode>>>,
    ) -> i64 {
        if let Some(n) = node {
            let n = n.borrow();
            let left = self.compute_subtree_sum(n.left.clone());
            let right = self.compute_subtree_sum(n.right.clone());

            let subtree_sum = n.val as i64 + left + right;

            let product = subtree_sum * (self.total_tree_sum - subtree_sum);
            self.max_product = self.max_product.max(product);

            subtree_sum
        } else {
            0
        }
    }

    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut sol = Solution {
            max_product: 0,
            total_tree_sum: 0,
        };

        sol.total_tree_sum = sol.compute_subtree_sum(root.clone());
        sol.compute_subtree_sum(root);

        (sol.max_product % MOD) as i32
    }
}
