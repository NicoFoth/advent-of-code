use std::collections::HashSet;
use std::fs;

fn main() {
    println!("Part 1: {}", solve_p1());
}

fn solve_p1() -> i32 {
    let contents = fs::read_to_string("src/input_p1.txt").unwrap();
    let lines: Vec<_> = contents.lines().map(|line| line.chars().collect::<Vec<char>>()).collect();

    let players = vec!['^', '>', 'v', '<'];
    let directions = vec![(-1, 0), (0, 1), (1, 0), (0, -1)];

    let mut obstacles: HashSet<(i32, i32)> = HashSet::new();
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    let mut start_position: (i32, i32) = (0, 0);
    let mut current_direction = (0, 0);

    for y in 0..lines.len() {
        for x in 0..lines[y].len() {
            let char: &char = &lines[y][x];
            if char == &'#' {
                obstacles.insert((y as i32, x as i32));
            } else if players.contains(char) {
                start_position = (y as i32, x as i32);
                let idx = players.iter().position(|c| c == &lines[y][x]).unwrap();
                current_direction = directions[idx];
            }
        }
    }

    let mut cur_pos = start_position;
    loop {
        let next_pos = (cur_pos.0 + current_direction.0, cur_pos.1 + current_direction.1);
        visited.insert(cur_pos);
        if next_pos.0 < 0 || next_pos.0 >= lines.len() as i32
            || next_pos.1 < 0 || next_pos.1 >= lines[0].len() as i32 {
            break;
        }

        let infront: &char = &lines[next_pos.0 as usize][next_pos.1 as usize];
        if infront == &'#' {
            current_direction = match current_direction {
                (-1, 0) => (0, 1),
                (0, 1) => (1, 0),
                (1, 0) => (0, -1),
                (0, -1) => (-1, 0),
                _ => (0, 0)
            }
        }
        cur_pos = (cur_pos.0 + current_direction.0, cur_pos.1 + current_direction.1)
    }

    visited.len() as i32
}