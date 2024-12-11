use std::collections::HashMap;
use std::fs;

fn main() {
    println!("Part 1: {:?}", solve_p1());
    println!("Part 2: {:?}", solve_p2());
}

fn apply_rule(engraving: &u64) -> Vec<u64>{
    let digit_count = engraving.checked_ilog10();
    if digit_count.is_none() {
        return vec![1]
    }
    let digit_count = digit_count.unwrap()+1;
    if engraving == &0 {
        vec![1]
    } else if digit_count % 2 == 0 {
        let divisor = 10u64.pow(digit_count - (digit_count / 2));
        vec![engraving / divisor, engraving % divisor]
    } else {
        vec![engraving*2024]
    }
}

fn solve_p1() -> usize {
    let contents = fs::read_to_string("src/input_p1.txt").unwrap();
    let mut stones: Vec<u64> = contents.split_whitespace().map(|x| x.parse::<u64>().unwrap()).collect();

    for _ in 0..25 {
        stones = stones.iter().flat_map(|stone| apply_rule(stone)).collect();
    }

    stones.len()
}

fn solve_p2() -> u64 {
    let contents = fs::read_to_string("src/input_p1.txt").unwrap();
    let mut stones: HashMap<u64, u64> = contents.split_whitespace().map(|x| (x.parse::<u64>().unwrap(), 1)).collect();

    for _ in 0..75 {
        let mut new_stones: HashMap<u64, u64> = HashMap::new();
        for stone in stones.keys() {
            let blinked_stones = apply_rule(stone);
            for blinked_stone in blinked_stones {
                new_stones
                    .entry(blinked_stone)
                    .and_modify(|val| *val += stones[stone])
                    .or_insert(stones[stone]);
            }
        }
        stones = new_stones.clone();
    }

    stones.values().sum()
}