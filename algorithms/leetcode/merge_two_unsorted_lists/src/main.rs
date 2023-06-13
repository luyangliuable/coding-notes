pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    fn new(val: i32) -> Self {
        ListNode {
            val,
            next: None
        }
    }
}

fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut res = Box::new(ListNode::new(0));
    let mut tail = &mut res;

    while let (Some(node1), Some(node2)) = (&list1, &list2) {
        if node1.val < node2.val {
            tail.next = list1;
            list1 = tail.next.as_mut().unwrap().next.take();
        } else {
            tail.next = list2;
            // Gets the next value of the next of that and take it so it because null.
            // .as_mut().unwrap() converts it into &mut Box<ListNode>
            list2 = tail.next.as_mut().unwrap().next.take();
        }

        // make tail equal to the next value which is not taken
        tail = tail.next.as_mut().unwrap();
    }

    tail.next = if list1.is_some() {list1} else {list2};

    res.next
}


fn test(mut head: Option<Box<ListNode>>) {
    let mut res = Box::new(ListNode::new(0));

    // tail is a mutable variable that contains a mutable reference to res
    // &mut means tail contains contains a mutable reference to res
    let mut tail = &mut res;

    // The expression Some(node) = &head tries to borrow head immutably and then immediately reassign its value,
    // which is not permitted.
    // Instead we use Some(node) = head.
    while let Some(mut node) = head.take() {
        println!("{}", node.val);
        tail = node.next.as_mut().unwrap();
        head = tail.next.take();
    }

    // while let Some(node) = head {
    //     println!("{}", node.val);
    //     tail.next = Some( node );
    //     tail = tail.next.as_mut().unwrap().next.as_mut().unwrap();
    //     head = tail.next.take();
    // }
}

fn main() {
    // Construct the first linked list: 1 -> 2 -> 4
    let list1 = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode {
                val: 4,
                next: None,
            })),
        })),
    }));

    // Construct the second linked list: 1 -> 3 -> 4
    let list2 = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 3,
            next: Some(Box::new(ListNode {
                val: 4,
                next: None,
            })),
        })),
    }));

    test(list1);

    // Merge the two lists
    // let result = merge_two_lists(list1, list2);

    // Print the merged list
    // print_list(result);

}

fn print_list(mut list: Option<Box<ListNode>>) {
    while let Some(node) = list {
        print!("{} ", node.val);
        list = node.next;
    }
    println!();
}

https://doc.rust-lang.org/stable/book/ch04-01-what-is-ownership.html
