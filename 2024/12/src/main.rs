use std::fs;
use std::collections::HashMap;
use std::collections::HashSet;


fn main() {
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2());
}

fn solve_p1() -> usize {
    let contents = fs::read_to_string("src/input_p1.txt").unwrap();
    let grid: Vec<Vec<char>> = contents.lines().map(|line| line.chars().collect()).collect();
    let mut total_price = 0;

    let mut visited = HashSet::new();

    for (y, row) in grid.iter().enumerate() {
        for (x, &cell) in row.iter().enumerate() {
            if cell == '.' || visited.contains(&(y, x)) {
                continue;
            }

            let region = flood_fill(&grid, y, x, &mut visited);
            
            let area = region.len();
            let perimeter = calculate_perimeter(&region, &grid);
            
            total_price += area * perimeter;
        }
    }

    total_price
}

fn solve_p2() -> usize {
    let contents = fs::read_to_string("src/input_p1.txt").unwrap();
    let grid: Vec<Vec<char>> = contents.lines().map(|line| line.chars().collect()).collect();
    let mut total_price = 0;

    let mut visited = HashSet::new();

    for (y, row) in grid.iter().enumerate() {
        for (x, &cell) in row.iter().enumerate() {
            if cell == '.' || visited.contains(&(y, x)) {
                continue;
            }

            let region = flood_fill(&grid, y, x, &mut visited);
            
            let area = region.len();
            let sides = calculate_sides(&region);
            
            total_price += area * sides;
        }
    }

    total_price
}

fn flood_fill(grid: &Vec<Vec<char>>, start_y: usize, start_x: usize, visited: &mut HashSet<(usize, usize)>) -> Vec<(usize, usize)> {
    let target_char = grid[start_y][start_x];
    let mut region = Vec::new();
    let mut stack = vec![(start_y, start_x)];

    while let Some((y, x)) = stack.pop() {
        if y >= grid.len() || x >= grid[0].len() || 
           grid[y][x] != target_char || 
           visited.contains(&(y, x)) {
            continue;
        }

        visited.insert((y, x));
        region.push((y, x));

        let directions = [(0, 1), (0, -1), (1, 0), (-1, 0)];
        for (dy, dx) in directions.iter() {
            let ny = y as i32 + dy;
            let nx = x as i32 + dx;

            if ny >= 0 && ny < grid.len() as i32 && 
               nx >= 0 && nx < grid[0].len() as i32 && 
               grid[ny as usize][nx as usize] == target_char {
                stack.push((ny as usize, nx as usize));
            }
        }
    }

    region
}

fn calculate_perimeter(region: &Vec<(usize, usize)>, grid: &Vec<Vec<char>>) -> usize {
    let mut perimeter = 0;
    let target_char = grid[region[0].0][region[0].1];

    for &(y, x) in region {
        let directions = [(0, 1), (0, -1), (1, 0), (-1, 0)];
        for (dy, dx) in directions.iter() {
            let ny = y as i32 + dy;
            let nx = x as i32 + dx;

            if ny < 0 || ny >= grid.len() as i32 || 
               nx < 0 || nx >= grid[0].len() as i32 || 
               grid[ny as usize][nx as usize] != target_char {
                perimeter += 1;
            }
        }
    }

    perimeter
}

fn calculate_sides(region: &Vec<(usize, usize)>) -> usize {
    let mut side_count = 0;
    let region: Vec<(i32, i32)> = region.iter().map(|x| (x.0 as i32, x.1 as i32)).collect();
    let directions = vec![(0, 1), (0, -1), (1, 0), (-1, 0)];
    for dir in directions {
        let mut sides: HashSet<(i32, i32)> = HashSet::new();
        for pos in &region {
            let tmp = (pos.0 + dir.0, pos.1 + dir.1);
            if !region.contains(&tmp) {
                sides.insert((tmp.0 as i32, tmp.1 as i32));
            }
        }
        let mut remove: HashSet<(i32, i32)> = HashSet::new();
        for side in &sides {
            let mut tmp = (side.0 + dir.1, side.1 + dir.0);
            while sides.contains(&tmp) {
                remove.insert(tmp);
                tmp = (tmp.0+ dir.1, tmp.1 + dir.0);
            }
        }
        side_count += sides.len() - remove.len();
    }

    side_count
}