use std::collections::{HashSet, VecDeque};
use std::fs;

fn main() {
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2());
}

fn get_reachable_positions(grid: &Vec<Vec<u32>>, current_position: (u32, u32)) -> Vec<(u32, u32)> {
    let directions: Vec<(i32, i32)> = vec![(1, 0), (-1, 0), (0, 1), (0, -1)];
    let mut reachable_positions: Vec<(u32, u32)> = Vec::new();
    let grid_length = grid.len();
    let grid_width = grid[0].len();

    for direction in directions {
        let new_position = (current_position.0 as i32 + direction.0, current_position.1 as i32 + direction.1);
        if new_position.0 >= 0 && new_position.0 < grid_width as i32
            && new_position.1 >= 0 && new_position.1 < grid_length as i32
            && grid[new_position.1 as usize][new_position.0 as usize] as i32 - grid[current_position.1 as usize][current_position.0 as usize] as i32 == 1 {
            reachable_positions.push((new_position.0 as u32, new_position.1 as u32));
        }
    }

    reachable_positions
}

fn build_grid() -> (Vec<Vec<u32>>, Vec<(u32, u32)>) {
    let contents = fs::read_to_string("src/input_p1.txt").unwrap();
    let mut grid: Vec<Vec<u32>> = Vec::new();
    let mut starts: Vec<(u32, u32)> = Vec::new();
    for (idy, line) in contents.lines().enumerate() {
        let mut row: Vec<u32> = Vec::new();
        for (idx, char) in line.chars().enumerate() {
            row.push(char.to_digit(10).unwrap());
            if char == '0' {
                starts.push((idx as u32, idy as u32))
            }
        }
        grid.push(row);
    }

    (grid, starts)
}

fn solve_p1() -> u32 {

    let (grid, starts) = build_grid();
    let mut sum = 0u32;

    for start in starts {
        let mut visited: HashSet<(u32, u32)> = HashSet::new();
        let mut queue: VecDeque<(u32, u32)> = VecDeque::new();
        queue.push_back(start);

        while !queue.is_empty() {
            let current = queue.pop_front().unwrap();
            if grid[current.1 as usize][current.0 as usize] == 9 {
                sum += 1;
            }

            let reachable = get_reachable_positions(&grid, current);
            for position in reachable {
                if !visited.contains(&position) {
                    queue.push_back(position);
                    visited.insert(position);
                }
            }
        }
    }

    sum
}

fn solve_p2() -> u32 {
    let (grid, starts) = build_grid();
    starts.iter().map(|start| dfs(start, &grid)).sum()
}

fn dfs(current_position: &(u32, u32), grid: &Vec<Vec<u32>>) -> u32 {
    if grid[current_position.1 as usize][current_position.0 as usize] == 9 {
        return 1;
    }
    let reachable = get_reachable_positions(&grid, *current_position);
    reachable.iter().map(|position| dfs(position, &grid)).sum()
}