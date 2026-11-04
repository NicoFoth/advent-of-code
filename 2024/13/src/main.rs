use std::fs;
use regex::Regex;

fn main() {
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2());
}

fn parse_input() -> Vec<((i64, i64), (i64, i64), (i64, i64))> {
    let contents = fs::read_to_string("src/input_p1.txt").unwrap();
    let lines: Vec<&str> = contents.lines().collect();
    let pattern = Regex::new(r"[+=](\d+)").unwrap();

    let mut input: Vec<((i64, i64), (i64, i64), (i64, i64))> = Vec::new();

    for line_idx in (0..lines.len()).step_by(4) {
        let mut x: Vec<(i64, i64)> = Vec::new();
        for i in 0..3 {
            let captures_a: Vec<_> = pattern.captures_iter(lines[line_idx + i]).collect();
            x.push((captures_a[0][1].parse::<i64>().unwrap(), captures_a[1][1].parse::<i64>().unwrap()));
        }
        input.push((x[0], x[1], x[2]));
    }

    input
}

fn solve_lgs(input: Vec<((i64, i64), (i64, i64), (i64, i64))>) -> i64 {
    let mut sum = 0;

    for (a, b, p) in input {
        let n = (p.0*b.1 - p.1*b.0) / (a.0*b.1 - a.1*b.0);
        let m = (a.0*p.1 - a.1*p.0) / (a.0*b.1 - a.1*b.0);

        if n*a.0 + m*b.0 == p.0 && n*a.1 + m*b.1 == p.1 {
            sum += 3*n+m;
        }
    }

    sum
}

fn solve_p1() -> i64 {
    let input = parse_input();
    solve_lgs(input)
}

fn solve_p2() -> i64 {
    let mut input = parse_input();
    let input = input.iter_mut().map(|(a, b, c)| {
        let new_c = (c.0 as i64 + 10000000000000, c.1 as i64 + 10000000000000);
        return ((a.0 as i64, a.1 as i64), (b.0 as i64, b.1 as i64), new_c)
    }).collect::<Vec<_>>();

    solve_lgs(input)
}