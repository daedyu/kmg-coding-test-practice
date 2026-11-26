// 3에서부터 시작해서 한계값 n이 되기 전까지 수 i를 증가시키면서,
// i%3==0 혹은 i%5==0이되는 수를 더해 나간다.

use std::collections::{HashMap, HashSet};
use std::io;

fn input() -> Vec<u32> {
    let mut buf = String::new();

    io::stdin().read_line(&mut buf).unwrap();

    buf.split_whitespace()
        .map(|s| s.parse::<u32>().unwrap())
        .collect()
}

fn main() {
    let nums = input();

    let n = nums[0];
    let m = nums[1];

    let mut edges: HashMap<u32, Vec<(u32, u32)>> = HashMap::new();

    for i in 1..(n+1) {
        edges.insert(i, vec![]);
    }

    for _ in 0..(n-1) {
        let nums = input();
        let (a, b, c) = (nums[0], nums[1], nums[2]);
        edges.entry(a).or_default().push((b, c));
        edges.entry(b).or_default().push((a, c));
    }

    for _ in 0..m {
        let nums = input();
        let (a, b) = (nums[0], nums[1]);
        println!("{}", dfs(a, b, &edges));
    }
}


fn dfs(node: u32, finish_node: u32, edges: &HashMap<u32, Vec<(u32, u32)>>) -> u32 {
    let mut stack: Vec<(u32, u32)> = Vec::new();
    let mut visited: HashSet<u32> = HashSet::new();

    stack.push((node, 0));

    while stack.len() > 0 {
        let (a, b) = stack.pop().unwrap();
        visited.insert(a);
        if a == finish_node {
            return b;
        }
        for (c, d) in edges.get(&a).unwrap() {
            if !visited.contains(c) {
                stack.push((*c, *d + b))
            }
        }
    }
    return 1
}