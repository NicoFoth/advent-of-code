use std::collections::HashSet;
use std::fs;
use std::hash::Hash;

const DIR: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];

fn main() {
    println!("Part 1: {}", solve_p1());
}

fn parse_input() -> (HashSet<(i32, i32)>, (i32, i32), (i32, i32)) {
    let contents = fs::read_to_string("src/input_p1.txt").unwrap();
    let lines: Vec<Vec<char>> = contents.lines().map(|line| line.chars().collect()).collect();
    let mut walls: HashSet<(i32, i32)> = HashSet::new();
    let mut start: (i32, i32) = (0, 0);
    let mut end: (i32, i32) = (0, 0);

    for y in 0..lines.len() {
        for x in 0..lines[y].len() {
            if lines[y][x] == '#' {
                walls.insert((y as i32, x as i32));
            } else if lines[y][x] == 'S' {
                start = (y as i32, x as i32);
            } else if lines[y][x] == 'E' {
                end = (y as i32, x as i32);
            }
        }
    }

    (walls, start, end)
}

fn solve_p1() -> i32 {
    let (walls, start, end) = parse_input();
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    visited.insert(start);
    dfs(&walls, &visited, start, (0, 1), end, 0)
}

fn dfs(walls: &HashSet<(i32, i32)>, visited: &HashSet<(i32, i32)>, current_position: (i32, i32), current_direction: (i32, i32), end: (i32, i32), current_points: i32) -> i32 {
    if current_position == end {
        return current_points;
    }
    let mut scores = Vec::new();
    let mut possible_directions = match current_direction {
        (1, 0) | (-1, 0) => vec![(0, 1), (0, -1)],
        (0, 1) | (0, -1) => vec![(1, 0), (-1, 0)],
        _ => vec![(0, 0)]
    };
    possible_directions.push(current_direction);
    for dir in possible_directions {
        let new_pos = (current_position.0 + dir.0, current_position.1 + dir.1);
        let mut new_points = current_points + 1;
        if current_direction != dir {
            new_points += 1000;
        }
        if !walls.contains(&new_pos) && !visited.contains(&new_pos){
            let mut new_visited = visited.clone();
            new_visited.insert(new_pos);
            scores.push(dfs(walls, &new_visited, new_pos, dir, end, new_points));
        }
    }

    *scores.iter().min().unwrap_or(&i32::MAX)
}

fn bfs(walls: &HashSet<(i32, i32)>, start: (i32, i32), end: (i32, i32)) -> i32 {
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    let mut queue: Vec<(i32, i32)> = Vec::new();
    queue.insert(0, start);

    while !queue.is_empty() {
        let current_position = queue.pop().unwrap();
        if current_position == end {
            return 6;
        }


    }

    5
}