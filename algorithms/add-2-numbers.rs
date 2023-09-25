// Definition for singly-linked list.

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    match (l1, l2) {
        (Some( n1 ), Some(n2)) => {
            let sum = n1.val + n2.val;

            if (sum < 10) {
                Some(Box::new(ListNode{
                    val: sum,
                    next: add_two_numbers(n1.next, n2.next)
                }))
            } else {
                let carry = Some(Box::new(ListNode::new(1)));

                Some(Box::new(ListNode {
                    val: sum - 10,
                    next: add_two_numbers(add_two_numbers(carry, n1.next), n2.next)
                }))
            }

        },
        (Some(n), None) => Some(n),
        (None, Some(n) ) => Some(n),
        (None, None) => None
    }
}

pub fn main() {
    let h1 = Some(Box::new(ListNode { val: 12, next: Some(Box::new(ListNode { val: 3, next: Some(Box::new(ListNode { val: 4, next: None } )) })) }));
    let h2 = Some(Box::new(ListNode { val: 1, next: Some(Box::new(ListNode { val: 3, next: Some(Box::new(ListNode { val: 4, next: None } )) })) }));

    let mut res = add_two_numbers(h1, h2);

    while res.is_some() {
        match ( res ) {
            Some(a) => {
                println!("{}", a.val);
                res = a.next;
            },
            None => continue
        };
    };
}
