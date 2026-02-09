use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

type Node = Option<Rc<RefCell<TreeNode>>>;

fn inorder(root: &Node, nodes: &mut Vec<Rc<RefCell<TreeNode>>>) {
    if let Some(n) = root {
        let left = n.borrow().left.clone();
        inorder(&left, nodes);
        nodes.push(n.clone());
        let right = n.borrow().right.clone();
        inorder(&right, nodes);
    }
}

fn build(nodes: &Vec<Rc<RefCell<TreeNode>>>, left: isize, right: isize) -> Node {
    if left > right {
        return None;
    }
    let mid = (left + right) / 2;
    let root = nodes[mid as usize].clone();
    root.borrow_mut().left = build(nodes, left, mid - 1);
    root.borrow_mut().right = build(nodes, mid + 1, right);
    Some(root)
}

pub fn balance_bst(root: Node) -> Node {
    let mut nodes = Vec::new();
    inorder(&root, &mut nodes);
    build(&nodes, 0, nodes.len() as isize - 1)
}
