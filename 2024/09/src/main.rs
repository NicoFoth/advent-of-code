use std::collections::HashMap;
use std::fs;

fn main() {
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2());
}

fn parse_input() -> Vec<i64> {
    let contents = fs::read_to_string("input.txt").unwrap();
    let numbers: Vec<i64> = contents.chars().map(|x| x.to_digit(10).unwrap() as i64).collect();
    let mut id = 0;
    let mut disk = Vec::new();
    for i in 0..contents.len() {
        if i % 2 == 0 {
            for _ in 0..numbers[i] {
                disk.push(id);
            }
            id += 1;
        } else {
            for _ in 0..numbers[i] {
                disk.push(-1);
            }
        }

    }

    disk
}

fn solve_p1() -> i64 {
    let mut disk = parse_input();
    let free_space = disk.iter().filter(|x| x == &&-1).count();

    for _ in 0..free_space {
        while disk.last().is_some() && disk.last().unwrap() == &-1 {
            disk.pop();
        }
        let last = disk.pop().unwrap();
        let idx = disk.iter().position(|x| x == &-1);
        if idx.is_none() {
            disk.push(last);
            break;
        }

        disk[idx.unwrap()] = last;
    }

    disk.iter().enumerate().map(|(i, e)| i as i64 * e).sum()
}

fn solve_p2() -> i64 {
    let mut disk = parse_input();
    let mut free_space: HashMap<i64, i64> = HashMap::new();
    let mut used_space: HashMap<i64, i64> = HashMap::new();
    println!("{:?}", disk);

    // Get the free_space hashmap
    let mut free_streak = 0;
    let mut free_streak_start = 0;
    for i in 0..disk.len() {
        if disk[i] == -1 {
            if free_streak == 0 {
                free_streak_start = i;
            }
            free_streak += 1;
        } else if free_streak > 0 {
            free_space.insert(free_streak_start as i64, free_streak);
            free_streak = 0;
        }
    }
    for (key, value) in &free_space {
        println!("{}: {}", key, value);
    }
    // Get the used_space hashmap
    let mut used_streak = 0;
    let mut used_streak_start = 0;
    let mut current_block_item = -1;
    for i in 0..disk.len() {
        if disk[i] == current_block_item{
            used_streak += 1;
        } else if used_streak > 0 {
            used_space.insert(used_streak_start as i64, used_streak);
            used_streak = 0;
            current_block_item = -1;
        } else if current_block_item == -1 {
            current_block_item = disk[i];
            used_streak += 1;
            used_streak_start = i;
        }
    }
    if used_streak > 0 {
        used_space.insert(used_streak_start as i64, used_streak);
    }
    println!("---");
    for (key, value) in &used_space {
        println!("{}: {}", key, value);
    }

    for _ in 0..free_space.len() {
        while disk.last().is_some() && disk.last().unwrap() == &-1 {
            disk.pop();
        }
        let last = disk.pop().unwrap();
        let idx = disk.iter().position(|x| x == &-1);
        if idx.is_none() {
            disk.push(last);
            break;
        }

        disk[idx.unwrap()] = last;
    }

    disk.iter().enumerate().map(|(i, e)| i as i64 * e).sum()
}