mod day1 {
static INPUT: std::sync::LazyLock<String> = std::sync::LazyLock::new(|| std::fs::read_to_string("input.txt").expect("input.txt"));

pub fn part1() -> usize {
    let mut zeros: usize = 0;
    let mut cur_pointer: i32 = 50;

    for line in INPUT.lines() {
        let (direction, distance) = line.split_at(1);
        let n = distance.parse::<i32>().expect("bad input");
        let delta = match direction { "R" => n, _ => -n };
        cur_pointer += delta;
        let remainder = cur_pointer.rem_euclid(100);

        zeros += cur_pointer.div_euclid(100).abs() as usize;

        cur_pointer = remainder;
    }

    zeros
}

pub fn part2() -> usize {
    0
}
}

fn main() {
    println!("day1 part1: {}", day1::part1());
    println!("day1 part2: {}", day1::part2());
}
