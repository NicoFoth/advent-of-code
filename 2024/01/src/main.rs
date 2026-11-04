use std::arch::x86_64::_xgetbv;
use std::fs;

fn main() {
    println!("Hello, world!");
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2())
}


fn solve_p1() -> i32 {
    let contents = fs::read_to_string("src/input_p1.txt")
        .expect("Should have been able to read the file");
    let lines: Vec<&str> = contents.lines().collect();

    let mut sum = 0;
    let mut list1: Vec<i32> = Vec::new();
    let mut list2: Vec<i32> = Vec::new();

    for line in lines {
        let splits: Vec<&str> = line.split_whitespace().collect();
        list1.push(splits[0].parse().unwrap());
        list2.push(splits[1].parse().unwrap());
    }

    list1.sort();
    list2.sort();

    for i in 0..list1.len() {
        sum += (list1[i] - list2[i]).abs();
    }

    sum
}

fn solve_p2() -> i32 {
    let contents = fs::read_to_string("src/input_p2.txt")
        .expect("Should have been able to read the file");
    let lines: Vec<&str> = contents.lines().collect();

    let mut sum = 0;
    let mut list1: Vec<i32> = Vec::new();
    let mut list2: Vec<i32> = Vec::new();

    for line in lines {
        let splits: Vec<&str> = line.split_whitespace().collect();
        list1.push(splits[0].parse().unwrap());
        list2.push(splits[1].parse().unwrap());
    }

    for i in 0..list1.len() {
        sum += list1[i] * list2.iter().filter(|&&x| x == list1[i]).count() as i32;
    }

    sum as i32
}

