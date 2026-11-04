use std::collections::HashSet;
use std::fs;

fn main() {
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2());
}

fn solve_p1() -> i32 {
    let contents = fs::read_to_string("input.txt").unwrap();
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

fn solve_p2() -> i32 {
    let contents = fs::read_to_string("input.txt").unwrap();
    let lines: Vec<_> = contents.lines().map(|line| line.chars().collect::<Vec<char>>()).collect();

    let players = vec!['^', '>', 'v', '<'];
    let directions = vec![(-1, 0), (0, 1), (1, 0), (0, -1)];

    let mut obstacles: HashSet<(i32, i32)> = HashSet::new();
    let mut start_position: (i32, i32) = (0, 0);
    let mut start_direction = (0, 0);

    for y in 0..lines.len() {
        for x in 0..lines[y].len() {
            let char: &char = &lines[y][x];
            if char == &'#' {
                obstacles.insert((y as i32, x as i32));
            } else if players.contains(char) {
                start_position = (y as i32, x as i32);
                let idx = players.iter().position(|c| c == char).unwrap();
                start_direction = directions[idx];
            }
        }
    }

    // Get original path
    let path = get_path(start_position, start_direction, &obstacles, &lines);
    let mut valid_positions = 0;

    // Only try positions along the original path
    for &pos in &path {
        if pos == start_position {
            continue;
        }

        obstacles.insert(pos);
        if creates_loop(start_position, start_direction, &obstacles, &lines) {
            valid_positions += 1;
        }
        obstacles.remove(&pos);
    }

    valid_positions
}

fn get_path(
    start: (i32, i32),
    start_dir: (i32, i32),
    obstacles: &HashSet<(i32, i32)>,
    lines: &Vec<Vec<char>>
) -> HashSet<(i32, i32)> {
    let mut path = HashSet::new();
    let mut cur_pos = start;
    let mut cur_dir = start_dir;

    while cur_pos.0 >= 0 && cur_pos.0 < lines.len() as i32
        && cur_pos.1 >= 0 && cur_pos.1 < lines[0].len() as i32 {
        path.insert(cur_pos);

        let next_pos = (cur_pos.0 + cur_dir.0, cur_pos.1 + cur_dir.1);
        if next_pos.0 < 0 || next_pos.0 >= lines.len() as i32
            || next_pos.1 < 0 || next_pos.1 >= lines[0].len() as i32 {
            break;
        }
        if obstacles.contains(&next_pos) {
            cur_dir = match cur_dir {
                (-1, 0) => (0, 1),
                (0, 1) => (1, 0),
                (1, 0) => (0, -1),
                (0, -1) => (-1, 0),
                _ => panic!("Invalid direction")
            };
        } else {
            cur_pos = next_pos;
        }
    }

    path
}

fn creates_loop(
    start: (i32, i32),
    start_dir: (i32, i32),
    obstacles: &HashSet<(i32, i32)>,
    lines: &Vec<Vec<char>>
) -> bool {
    let mut visited: HashSet<((i32, i32), (i32, i32))> = HashSet::new();
    let mut cur_pos = start;
    let mut cur_dir = start_dir;

    loop {
        let state = (cur_pos, cur_dir);
        if visited.contains(&state) {
            return true;
        }
        visited.insert(state);

        let next_pos = (cur_pos.0 + cur_dir.0, cur_pos.1 + cur_dir.1);

        // Check if out of bounds
        if next_pos.0 < 0 || next_pos.0 >= lines.len() as i32
            || next_pos.1 < 0 || next_pos.1 >= lines[0].len() as i32 {
            return false;
        }

        // Check if hitting obstacle
        if obstacles.contains(&next_pos) {
            cur_dir = match cur_dir {
                (-1, 0) => (0, 1),  // facing up -> turn right
                (0, 1) => (1, 0),   // facing right -> turn down
                (1, 0) => (0, -1),  // facing down -> turn left
                (0, -1) => (-1, 0), // facing left -> turn up
                _ => panic!("Invalid direction")
            };
        } else {
            cur_pos = next_pos;
        }
    }
}