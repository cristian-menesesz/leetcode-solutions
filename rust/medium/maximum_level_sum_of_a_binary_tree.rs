use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

#[derive(Debug)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    let root = match root {
        Some(r) => r,
        None => return 0,
    };

    let mut queue = VecDeque::new();
    queue.push_back(root);
    
    let mut max_sum = i32::MIN;
    let mut best_level = 0;
    let mut current_level = 1;

    while !queue.is_empty() {
        let level_size = queue.len();
        let mut level_sum = 0;

        for _ in 0..level_size {
            let node = queue.pop_front().unwrap();
            let node_ref = node.borrow();
            level_sum += node_ref.val;

            if let Some(left) = &node_ref.left {
                queue.push_back(left.clone());
            }
            if let Some(right) = &node_ref.right {
                queue.push_back(right.clone());
            }
        }

        if level_sum > max_sum {
            max_sum = level_sum;
            best_level = current_level;
        }

        current_level += 1;
    }

    best_level
}
