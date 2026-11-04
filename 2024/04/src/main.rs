use std::collections::HashMap;
use std::fs;

fn main() {
    println!("Part 1: {}", solve_p1());
    println!("Part 2: {}", solve_p2());
}

fn check_for_needle(padded_lines: &Vec<String>, needle: &Vec<char>) -> i32 {
    // Directions in (x, y) format right - x+, down - y+, down-right - x+y+, up-right - x+y-
    let directions = vec![(1, 0), (0, 1), (1, 1), (1, -1)];

    let mut sum = 0;
    for y in 1..padded_lines.len() {
        for x in 1..padded_lines[y].len() {
            if padded_lines[y].chars().nth(x).unwrap() == needle[0] {
                'dirloop: for (dx, dy) in &directions {
                    for (i, c) in needle.iter().enumerate() {
                        let cur_x = (dx*i as i32 + (x as i32)) as usize;
                        let cur_y = (dy*i as i32 + (y as i32)) as usize;
                        if padded_lines[cur_y].chars().nth(cur_x).unwrap() != *c {
                            continue 'dirloop;
                        }
                    }
                    sum += 1;
                }
            }
        }
    }

    sum
}

fn solve_p1() -> i32 {
    let contents = fs::read_to_string("src/input_p1.txt");
    // Create padding before and after every line
    let lines = contents.unwrap().lines().map(|x| format!(".{x}.")).collect::<Vec<String>>();
    // Create padding before and after the whole input
    let mut padded_lines = vec![".".repeat(lines[0].len())];
    padded_lines.extend(lines);
    padded_lines.push(padded_lines[0].clone());
    let padded_lines_reverse = padded_lines.iter().map(|x| x.chars().rev().collect::<String>()).rev().collect::<Vec<String>>();

    let needle = vec!['X', 'M', 'A', 'S'];
    let mut sum = 0;
    sum += check_for_needle(&padded_lines, &needle);
    sum += check_for_needle(&padded_lines_reverse, &needle);

    sum
}

fn solve_p2() -> i32 {
    let contents = fs::read_to_string("src/input_p1.txt");
    let lines = contents.unwrap().lines().map(|x| format!(".{x}.")).collect::<Vec<String>>();
    let mut padded_lines = vec![".".repeat(lines[0].len())];
    padded_lines.extend(lines);
    padded_lines.push(padded_lines[0].clone());

    let directions: Vec<(i32, i32)> = vec![(1, 1), (-1, 1)];
    let opposing_directions: HashMap<(i32, i32), (i32, i32)> = [
        ((1, 1), (-1, -1)),
        ((-1, -1), (1, 1)),
        ((1, -1), (-1, 1)),
        ((-1, 1), (1, -1))
    ].into_iter().collect();

    let mut sum = 0;
    for y in 1..padded_lines.len() {
        'search: for x in 1..padded_lines[y].len() {
            if padded_lines[y].chars().nth(x).unwrap() == 'A' {
                for (dx, dy) in &directions {
                    let c = padded_lines[(y as i32 + *dy) as usize].chars().nth((x as i32 + *dx) as usize).unwrap();
                    let expected_opposing = match c {
                        'M' => 'S',
                        'S' => 'M',
                        _ => '*'
                    };
                    let opposing_coords = opposing_directions.get(&(*dy, *dx)).unwrap();
                    if padded_lines[(y as i32 + opposing_coords.0) as usize].chars().nth((x as i32 + opposing_coords.1) as usize).unwrap() != expected_opposing {
                        continue 'search;
                    }
                }
                sum += 1;
            }
        }
    }




    sum
}