use std::cmp::Ordering;
use std::fs;

fn main() {
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2());
}

fn parse_input() -> (Vec<(i32, i32)>, Vec<Vec<i32>>) {
    let contents = fs::read_to_string("src/input_p1.txt").unwrap();
    let (rules, updates) = contents.split_once("\n\n").unwrap();
    let rules = rules
        .lines()
        .map(|line| line.split_once("|").unwrap())
        .map(|(l, r)| (l.parse::<i32>().unwrap(), r.parse::<i32>().unwrap()))
        .collect::<Vec<_>>();

    let updates = updates
        .lines()
        .map(|line| line.split(",")
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<_>>())
        .collect::<Vec<_>>();

    (rules, updates)
}

fn solve_p1() -> i32 {
    let (rules, updates) = parse_input();

    updates
        .into_iter()
        .filter(|pages| {
            pages.is_sorted_by(|a, b| !rules.contains(&(*b, *a)))
        })
        .map(|pages| pages[pages.len()/2])
        .sum()
}

fn solve_p2() -> i32 {
    let (rules, updates) = parse_input();

    updates
        .into_iter()
        .filter(|pages| {
            !pages.is_sorted_by(|a, b| !rules.contains(&(*b, *a)))
        })
        .map(|mut update| {
            update.sort_by(|a, b| {
                if rules.contains(&(*a, *b)) {
                    Ordering::Greater
                } else if rules.contains(&(*b, *a)) {
                    Ordering::Less
                } else {
                    Ordering::Equal
                }
            });
            update
        })
        .map(|pages| pages[pages.len()/2])
        .sum()
}