use std::collections::HashSet;
use std::fs;
use regex::Regex;

const WIDTH: i32 = 101;
const LENGTH: i32 = 103;

fn main() {
    println!("Part 1: {}", solve_p1());
    solve_p2_2();
}

fn parse_input() -> Vec<((i32, i32), (i32, i32))> {
    let contents = fs::read_to_string("input.txt").unwrap();
    let pattern = Regex::new(r"p=(\d+,\d+) v=(-?\d+,-?\d+)").unwrap();
    let mut robots: Vec<((i32, i32), (i32, i32))> = Vec::new();

    for line in contents.lines() {
        let captures: Vec<_> = pattern.captures_iter(line).collect();
        let pos: &Vec<i32> = &captures[0][1].split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        let vel: &Vec<i32> = &captures[0][2].split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        robots.push(((pos[0], pos[1]), (vel[0], vel[1])))
    }

    robots
}

fn calculate_positions(seconds: i32) -> (HashSet<(i32, i32)>, i32, i32, i32, i32) {
    let robots = parse_input();
    let mut future_robots: HashSet<(i32, i32)> = HashSet::new();
    let mut q1 = 0;
    let mut q2 = 0;
    let mut q3 = 0;
    let mut q4 = 0;

    for robot in robots {
        let mut nx = (robot.0.0 + seconds*robot.1.0) % WIDTH;
        if nx < 0 {
            nx = WIDTH+nx;
        }
        let mut ny = (robot.0.1 + seconds*robot.1.1) % LENGTH;
        if ny < 0 {
            ny = LENGTH+ny;
        }
        future_robots.insert((nx, ny));

        if nx == WIDTH/2 || ny == LENGTH/2 {
            continue;
        }
        match (nx <= WIDTH/2, ny <=LENGTH/2) {
            (true, true) => q1 += 1,
            (false, true) => q2 += 1,
            (true, false) => q3 += 1,
            (false, false) => q4 += 1
        }
    }

    (future_robots, q1, q2, q3, q4)
}

fn solve_p1() -> i32 {
    let (_, q1, q2, q3, q4) = calculate_positions(100);
    q1 * q2 * q3 * q4
}

fn solve_p2() {
    let mut print = "".to_owned();
    for i in 1000..10000 {
        let (future_robots, _, _, _, _) = calculate_positions(i);
        print.push_str(&*i.to_string());
        print.push_str("\n");
        for i in 0..LENGTH {
            for j in 0..WIDTH {
                if future_robots.contains(&(j, i)) {
                    print.push_str("1");
                } else {
                    print.push_str(".");
                }
            }
            print.push_str("\n");
        }
        print.push_str("\n");
    }
    fs::write("aoc.txt", print).expect("Unable");
}

fn solve_p2_2() -> i32 {
    let robot_amount = fs::read_to_string("input.txt").unwrap().lines().count();
    for i in 0..10000 {
        let (future_robots, _, _, _, _) = calculate_positions(i);
        if future_robots.len() == robot_amount {
            return i
        }
    }

    -1
}