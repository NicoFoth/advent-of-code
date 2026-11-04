use std::fs;
use regex::Regex;

fn main() {
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2());
}

fn sum_multiplications(input: &str) -> i32 {
    Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)")
        .unwrap()
        .captures_iter(input)
        .map(|cap| cap[1].parse::<i32>().unwrap() * cap[2].parse::<i32>().unwrap())
        .sum()
}

fn solve_p1() -> i32 {
    let contents = fs::read_to_string("src/input_p1.txt")
        .expect("Should have been able to read the file");

    sum_multiplications(&contents)
}

fn solve_p2() -> i32 {
    let contents = fs::read_to_string("src/input_p1.txt")
        .expect("Should have been able to read the file");

    let mut segments = contents.split("don't()");
    let first_segment = sum_multiplications(segments.next().unwrap_or(""));
    let sum = segments.fold(first_segment, |acc, segment| {
        acc + sum_multiplications(&segment[segment.find("do()").unwrap_or(segment.len())..])
    });

    sum
}