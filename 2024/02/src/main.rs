use std::fs;

fn main() {
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2());
}


fn solve_p1() -> i32 {
    let contents = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");
    let lines: Vec<&str> = contents.lines().collect();

    let mut sum = 0;
    for line in lines {
        let levels: Vec<i32> = line
            .split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect();
        
        if check_report(&levels) {
            sum += 1;
        }
    }

    sum
}

fn solve_p2() -> i32 {
    let contents = fs::read_to_string("input.txt")
        .expect("Should have been able to read the file");
    let lines: Vec<&str> = contents.lines().collect();

    let mut sum = 0;
    for line in lines {
        let levels: Vec<i32> = line
            .split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect();
        
        if check_report_with_dampener(levels) {
            sum += 1;
        }
    }

    sum
}

fn check_report(levels: &Vec<i32>) -> bool {
    let mut prev = levels[0];

    let ascending = levels.windows(2).all(|w| w[0] < w[1]);
    let descending = levels.windows(2).all(|w| w[0] > w[1]);
    if ascending || descending {
        for i in 1..levels.len() {
            if (levels[i] - prev).abs() > 3 {
                return false;
                }
                prev = levels[i] as i32;
            }

        return true;
    }
    return false;
}

fn check_report_with_dampener(levels: Vec<i32>) -> bool {
    if check_report(&levels) {
        return true;
    }

    for i in 0..levels.len() {
        let mut modified_levels = levels.clone();
        modified_levels.remove(i);
        
        if check_report(&modified_levels) {
            return true;
        }
    }

    false
}